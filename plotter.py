import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


class DistributionPlotter:
    @staticmethod
    def ordinal(n): #turn a position number into an ordinal label (1 -> 1st, 2 -> 2nd ...)
        if 10 <= n % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return f"{n}{suffix}"

    def plot(self, distribution, hand):
        #index i = probability that exactly i opponents have a stronger preflop hand,
        #which puts the user in finishing position i + 1.
        positions = [self.ordinal(i + 1) for i in range(len(distribution))]
        best_index = max(range(len(distribution)), key=lambda i: distribution[i])

        highlight = "#2a9d8f"
        base = "#a8c5c0"
        colors = [highlight if i == best_index else base for i in range(len(distribution))]

        fig, ax = plt.subplots(figsize=(max(6, len(distribution) * 0.9), 5))
        bars = ax.bar(positions, distribution, color=colors, edgecolor="white", linewidth=1.2, zorder=3)

        for rect, prob in zip(bars, distribution):
            ax.annotate(f"{prob:.1%}",
                        xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()),
                        xytext=(0, 4), textcoords="offset points",
                        ha="center", va="bottom", fontsize=10, color="#264653")

        ax.set_title(f"Finishing position distribution for {hand}", fontsize=14, fontweight="bold", color="#264653", pad=14)
        ax.set_xlabel("Finishing position (by preflop hand strength)", fontsize=11, color="#264653")
        ax.set_ylabel("Probability", fontsize=11, color="#264653")
        ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0))
        ax.set_ylim(0, max(distribution) * 1.18)

        ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(colors="#264653")

        fig.tight_layout()
        plt.show()
