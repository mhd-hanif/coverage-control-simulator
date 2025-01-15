def save_plot_as_image(fig, filepath):
    """
    Save a matplotlib figure as an image file.
    
    Parameters:
        fig (matplotlib.figure.Figure): The figure to save.
        filepath (str): Path to save the image.
    """
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
