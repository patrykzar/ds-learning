"""
Moduł do tworzenia wykresów danych.
Zawiera funkcje do rysowania histogramów, scatter plot'ów i line plot'ów.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_histogram(data, title="Histogram", bins=20, color="skyblue"):
    """
    Rysuje histogram rozkładu danych.
    
    Args:
        data (list/array): Dane do wykreślenia
        title (str): Tytuł wykresu
        bins (int): Liczba przedziałów (default: 20)
        color (str): Kolor słupków (default: skyblue)
    
    Returns:
        None (wyświetla wykres)
    
    Example:
        >>> data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        >>> plot_histogram(data, "Moje dane")
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, color=color, edgecolor="black", alpha=0.7)
    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel("Wartość", fontsize=12)
    plt.ylabel("Częstość", fontsize=12)
    plt.grid(axis="y", alpha=0.3, linestyle="--")
    plt.tight_layout()
    plt.show()


def plot_scatter(x_data, y_data, title="Scatter Plot", color="red", size=50):
    """
    Rysuje scatter plot (punkt po punkcie).
    
    Args:
        x_data (list/array): Dane na osi X
        y_data (list/array): Dane na osi Y
        title (str): Tytuł wykresu
        color (str): Kolor punktów (default: red)
        size (int): Rozmiar punktów (default: 50)
    
    Returns:
        None (wyświetla wykres)
    
    Example:
        >>> x = [1, 2, 3, 4, 5]
        >>> y = [2, 4, 5, 4, 6]
        >>> plot_scatter(x, y, "X vs Y")
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color=color, s=size, alpha=0.6, edgecolors="black")
    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.grid(alpha=0.3, linestyle="--")
    plt.tight_layout()
    plt.show()


def plot_line(x_data, y_data, title="Line Plot", color="blue", linewidth=2):
    """
    Rysuje line plot (linia czasowa lub zależności).
    
    Args:
        x_data (list/array): Dane na osi X
        y_data (list/array): Dane na osi Y
        title (str): Tytuł wykresu
        color (str): Kolor linii (default: blue)
        linewidth (int): Grubość linii (default: 2)
    
    Returns:
        None (wyświetla wykres)
    
    Example:
        >>> x = [1, 2, 3, 4, 5]
        >>> y = [2, 4, 5, 4, 6]
        >>> plot_line(x, y, "Trend")
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker="o", color=color, 
             linewidth=linewidth, markersize=8, alpha=0.8)
    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.grid(alpha=0.3, linestyle="--")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Przykład użycia
    print("Tworzenie przykładowych wykresów...")
    
    # Histogram
    data = np.random.normal(100, 15, 1000)
    plot_histogram(data, "Rozkład normalny")
    
    # Scatter plot
    x = np.random.rand(50) * 10
    y = 2 * x + np.random.normal(0, 2, 50)
    plot_scatter(x, y, "Zależność liniowa")
    
    # Line plot
    x_line = np.linspace(0, 10, 100)
    y_line = np.sin(x_line)
    plot_line(x_line, y_line, "Fala sinusoidalna")
