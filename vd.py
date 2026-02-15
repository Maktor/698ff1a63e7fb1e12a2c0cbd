import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))

    fig.patch.set_facecolor('#E6E6E6')
    ax.set_facecolor('#E6E6E6')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'],
            circle['radius'],
            linewidth=6,
            edgecolor='black',
            facecolor='none'
        )
        ax.add_patch(c)

    text_elements = [
        (0.20, 0.70, 'K', 'black', 35),
        (0.19, 0.60, 'M', 'black', 35),
        (0.29, 0.55, 'T', 'blue', 35),
        (0.26, 0.75, 'H', 'black', 35),

        (0.80, 0.70, 'Q', 'black', 35),
        (0.81, 0.61, 'G', 'black', 35),
        (0.72, 0.59, 'D', 'black', 35),
        (0.76, 0.77, 'P', 'black', 35),
        (0.51, 0.09, 'β', 'black', 40),
        (0.41, 0.14, 'λ', 'black', 40),
        (0.59, 0.17, 'δ', 'black', 40),
        (0.49, 0.23, 'τ', 'green', 40),
        (0.51, 0.72, 'L', 'black', 35),
        (0.49, 0.62, 'Y', 'red', 35),
        (0.52, 0.57, 'U', 'black', 35),

        (0.31, 0.41, 'Δ', 'black', 40),
        (0.38, 0.31, 'Ξ', 'black', 40),
        (0.29, 0.34, 'Σ', 'black', 40),

        (0.67, 0.42, 'θ', 'black', 40),
        (0.62, 0.31, 'α', 'black', 40),
        (0.76, 0.38, 'ρ', 'black', 40),

        (0.50, 0.45, '!', 'black', 45)
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char,
            color=color,
            fontsize=size,
            ha='center',
            va='center',
            fontfamily='serif',
            fontweight='bold'
        )

    # 4. Final Formatting
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # 5. Save/Show
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
