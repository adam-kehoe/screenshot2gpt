class Prompts(object):
    def __init__(self):
        self.science = """If this is scientific or technical in nature, please concisely 
        explain the content at the level of a bright high school student."""
        self.dalle = """Suggest a DALL-E prompt to get an image like this. Make sure to reference
        the most distinctive aspects of the overall art style with very specific words."""
        self.uiux = """Acting as a thoughtful UI/UX expert, please critique this interface.
        Rate the strength of the overall design on a scale of 1 to 10 and briefly explain the rating.
        Concisely provide at least 2 or 3 specific suggestions for improvement, and explain why
        they would improve the interface. Make at least one positive remark about the strongest
        aspect of the design."""
        self.fundamentals = """Identify the key academic fields related to this. Suggest 2-5 books
        that would be good for a beginner to read to learn more about this topic."""
        self.psychological = """Provide a psychological interpretation of the image. What subconscious
        themes might it touch on?"""
        self.electronics = """Identify the components in this image and their model
        numbers if possible."""
        self.math = """Explain the mathematics in this image step by step. If any specialized fields
        are represented, identify them and suggest further resources."""
