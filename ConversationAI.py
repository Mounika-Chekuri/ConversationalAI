import streamlit as st
import openai




st.title("Trip Planner AI with OpenAI and Streamlit")
client = openai.OpenAI()
#openai.api_key = api_key

# Initialize session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


# Define a function to interact with OpenAI's API
def get_openai_response(prompt, history):
    # Combine the history into a single prompt
    full_prompt = "\n".join(history) + f"\nYou: {prompt}\nAI: "

    try:
        from openai import OpenAI
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for trip planning."},
                {"role": "user", "content": full_prompt}
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "text"
            }
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# User input
user_input = st.text_input("Ask me anything about your trip: ", "")

# Display examples of questions for trip planning
st.markdown("""
**Example questions:**
- "What are the best places to visit in Europe during summer?"
- "Can you suggest a 5-day itinerary for Paris?"
- "What are some family-friendly activities in New York?"
- "Where can I find budget accommodations in Tokyo?"
- "What are the top attractions in Sydney?"
- "What’s the best time of year to visit Bali?"
""")

if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(f"You: {user_input}")
        ai_response = get_openai_response(user_input, st.session_state.chat_history)
        st.session_state.chat_history.append(f"AI: {ai_response}")
        for message in st.session_state.chat_history:
            st.write(message)
    else:
        st.write("Please enter a message.")

if st.button("Clear Chat"):
    st.session_state.chat_history = []

