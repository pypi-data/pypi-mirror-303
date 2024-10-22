import time
import torch
import pandas as pd
import matplotlib.pyplot as plt
from tinytopics.fit import fit_model
from tinytopics.utils import generate_synthetic_data, set_random_seed


set_random_seed(42)


n_values = [1000, 5000]  # Number of documents
m_values = [500, 1000, 5000, 10000]  # Vocabulary size
k_values = [10, 50, 100]  # Number of topics
learning_rate = 0.01
avg_doc_length = 256 * 256


benchmark_results = pd.DataFrame()


def benchmark(X, k, device):
    start_time = time.time()
    model, losses = fit_model(X, k, learning_rate=learning_rate, device=device)
    elapsed_time = time.time() - start_time

    return elapsed_time


for n in n_values:
    for m in m_values:
        for k in k_values:
            print(f"Benchmarking for n={n}, m={m}, k={k}...")

            X, true_L, true_F = generate_synthetic_data(
                n, m, k, avg_doc_length=avg_doc_length
            )

            # Benchmark on CPU
            cpu_time = benchmark(X, k, torch.device("cpu"))
            cpu_result = pd.DataFrame(
                [{"n": n, "m": m, "k": k, "device": "CPU", "time": cpu_time}]
            )

            if not cpu_result.isna().all().any():
                benchmark_results = pd.concat(
                    [benchmark_results, cpu_result], ignore_index=True
                )

            # Benchmark on GPU if available
            if torch.cuda.is_available():
                gpu_time = benchmark(X, k, torch.device("cuda"))
                gpu_result = pd.DataFrame(
                    [{"n": n, "m": m, "k": k, "device": "GPU", "time": gpu_time}]
                )

                if not gpu_result.isna().all().any():
                    benchmark_results = pd.concat(
                        [benchmark_results, gpu_result], ignore_index=True
                    )


benchmark_results.to_csv("benchmark-results.csv", index=False)


for k in k_values:
    plt.figure(figsize=(7, 4.3), dpi=300)

    for n in n_values:
        subset = benchmark_results[
            (benchmark_results["n"] == n) & (benchmark_results["k"] == k)
        ]

        plt.plot(
            subset[subset["device"] == "CPU"]["m"],
            subset[subset["device"] == "CPU"]["time"],
            label=f"CPU (n={n})",
            linestyle="--",
            marker="o",
        )
        if torch.cuda.is_available():
            plt.plot(
                subset[subset["device"] == "GPU"]["m"],
                subset[subset["device"] == "GPU"]["time"],
                label=f"GPU (n={n})",
                linestyle="-",
                marker="x",
            )

    plt.xlabel("Vocabulary Size (m)")
    plt.ylabel("Training Time (seconds)")
    plt.title(f"Training Time vs. Vocabulary Size (k={k})")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"training-time-k-{k}.png", dpi=300)
    plt.close()
