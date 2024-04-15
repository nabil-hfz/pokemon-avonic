class Formatter:
    """Utility class for various formatting tasks within the game."""

    @staticmethod
    def format_name(name):
        """Capitalize and trim the name for display."""
        return name.strip().title()

    @staticmethod
    def format_damage(damage):
        """Format damage to one decimal place to avoid floating-point precision issues."""
        return f"{damage:.1f}"

    @staticmethod
    def format_health(health):
        """Format health value to no decimal places."""
        return f"{health:.0f}"

    @staticmethod
    def format_percentage(value):
        """Format a percentage value to show up to two decimal places."""
        return f"{value:.2f}%"
