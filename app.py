import streamlit as st
import google.generativeai as genai
import random

# Make sure your Google API key is set
api_key =   # Replace this with your actual API key
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not set. Please configure your Google API key.")

# Create the model using Gemini 1.5 Flash
model = genai.GenerativeModel("gemini-1.5-flash")

# List of symbols and emojis for random selection based on the topic
symbols = ["🚀", "💡", "🎯", "🔥", "🌟", "📚", "💼", "🎓", "🤖", "📈", "🌱", "✨", "🎉"]

def generate_linkedin_post(input_text):
    """Function to call the Gemini API and get the generated content."""
    try:
        # Prepare the prompt to generate a creative title and 5 lines of content with hashtags starting on a new line
        prompt = f"Generate a creative, professional, and catchy LinkedIn post title with emojis and symbols for the topic: '{input_text}'. Then, write a 5-line post with emojis and symbols where appropriate. Add hashtags at the end on a new line."

        # Generate content using the model
        response = model.generate_content(prompt)
        generated_text = response.text.strip()

        # Separate the content and the hashtags
        content_lines = generated_text.split("\n")
        title = content_lines[0]  # First line should be the title
        content = "\n".join(content_lines[1:6])  # Get the next 5 lines for content
        hashtags = "\n" + "\n".join(content_lines[6:])  # Ensure hashtags are on a new line

        # Randomly select symbols for title, content, and hashtags
        random_symbol_title = random.choice(symbols)
        random_symbol_content = random.choice(symbols)
        random_symbol_hashtags = random.choice(symbols)

        # Add symbols to the title and content dynamically
        fancy_title = f"{random_symbol_title} **{title.upper()}** {random_symbol_title}"
        fancy_content = f"{random_symbol_content} {content} {random_symbol_content}"
        fancy_hashtags = f"{random_symbol_hashtags}\n{hashtags} {random_symbol_hashtags}"

        # Return the formatted creative title, content, and hashtags
        return f"### {fancy_title}\n\n{fancy_content}\n\n{fancy_hashtags}"
    except Exception as e:
        return f"Error generating content: {str(e)}"

# Streamlit UI
st.title('LinkedIn Post Generator')

st.write(
    "Welcome to the LinkedIn Post Generator! Enter a topic or statement, and the bot will generate a creative title and a professional post for you."
)

# Input field for the statement
input_statement = st.text_area("Enter your statement", "", key="input")

# Button to generate content
if st.button('Generate LinkedIn Post'):
    if input_statement:
        # Generate LinkedIn content using the Gemini API
        post_content = generate_linkedin_post(input_statement)
        st.subheader("Generated LinkedIn Post:")
        st.write(post_content)
    else:
        st.error("Please enter a statement to generate content.")

# Adding custom CSS for responsiveness
st.markdown("""
    <style>
        /* Responsive design for mobile and desktop */
        @media (max-width: 768px) {
            .css-1d391kg {
                font-size: 18px !important;
            }
            .css-1dq8tca {
                margin-top: 0px !important;
            }
            .css-13ne4p4 {
                padding: 10px !important;
            }
            .css-ffhzg2 {
                font-size: 18px !important;
            }
            .stTextArea textarea {
                font-size: 16px !important;
                padding: 10px;
                width: 100%;
            }
            .stButton button {
                font-size: 16px !important;
                padding: 12px 20px;
            }
        }
        
        /* Desktop styles */
        @media (min-width: 769px) {
            .css-1d391kg {
                font-size: 24px !important;
            }
            .css-1dq8tca {
                margin-top: 30px !important;
            }
            .css-13ne4p4 {
                padding: 20px !important;
            }
            .css-ffhzg2 {
                font-size: 22px !important;
            }
            .stTextArea textarea {
                font-size: 18px !important;
                width: 70%;
            }
            .stButton button {
                font-size: 18px !important;
                padding: 16px 24px;
            }
        }
    </style>
""", unsafe_allow_html=True)

