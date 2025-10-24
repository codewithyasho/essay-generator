import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from st_copy_to_clipboard import st_copy_to_clipboard 

load_dotenv()

st.title("✍️ Essay Generator")
st.markdown("Generate high-quality essays")

prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", """You are an expert essay writer with a talent for creating compelling, well-structured academic and creative essays. 
Your essays should:
- Have a clear introduction, body paragraphs, and conclusion
- Use varied sentence structures and sophisticated vocabulary
- Include relevant examples and logical arguments
- Flow smoothly with proper transitions
- Be engaging and maintain reader interest throughout
- Follow proper essay writing conventions"""),

        ("human", """Write a {words}-word essay on the topic: "{topic}" in {language} language.

Requirements:
1. Create an engaging and relevant title
2. Structure the essay with clear introduction, body, and conclusion
3. Use appropriate tone and style for the topic
4. Ensure the word count is close to {words} words
5. Make it informative, well-researched, and compelling

Begin with the title, then write the essay."""),
    ]
)

# llms
llm1 = ChatOllama(model="deepseek-v3.1:671b-cloud", temperature=0.7)
llm2 = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

chain = prompt1 | llm2 | StrOutputParser()

topic = st.text_input("Enter Topic: ")
words = st.text_input("Number of Words: ")
language = st.text_input("language: ")

if st.button("Submit"):
    if topic and words and language:
        with st.spinner("Generating your essay..."):
            result_placeholder = st.empty()
            full_text = ""

            for chunk in chain.stream({
                "topic": topic,
                "words": words,
                "language": language,
            }):
                full_text += chunk
                result_placeholder.markdown(full_text)

        st.balloons()

        # Display word count
        word_count = len(full_text.split())
        st.success(f"✅ Essay generated successfully! Word count: {word_count}")

        # Copy button
        st_copy_to_clipboard(full_text, "📋 Copy Essay")

    else:
        st.warning("Please fill in all fields!")

# Footer
st.markdown("---")
st.markdown("*Powered by LangChain, Groq & DeepSeek*")
