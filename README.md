# ✍️ Essay Generator

A powerful AI-powered essay generator built with Streamlit, LangChain, and advanced language models. Generate high-quality, well-structured essays on any topic in multiple languages.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)

## 🌟 Features

- **AI-Powered Generation**: Utilizes advanced language models (Groq's Llama and DeepSeek) for intelligent essay creation
- **Customizable Length**: Specify the desired word count for your essay
- **Multi-Language Support**: Generate essays in any language
- **Real-time Streaming**: Watch your essay being generated in real-time
- **Copy to Clipboard**: Easily copy the generated essay with one click
- **Professional Structure**: Essays include proper introduction, body paragraphs, and conclusion
- **Word Count Display**: Automatic word count tracking

## 🚀 Demo

The application generates essays with:
- Clear and engaging titles
- Well-structured content with proper flow
- Relevant examples and logical arguments
- Sophisticated vocabulary and varied sentence structures
- Proper essay writing conventions

## 📋 Prerequisites

- Python 3.8 or higher
- API keys for:
  - [Groq](https://console.groq.com/) (for Llama model)
  - [Ollama](https://ollama.ai/) (optional, for DeepSeek model)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/codewithyasho/essay-generator.git
   cd essay-generator
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install streamlit python-dotenv langchain-groq langchain-core langchain-ollama st-copy-to-clipboard
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   OLLAMA_BASE_URL=http://localhost:11434  # Optional, if using Ollama
   ```

## 🎯 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Generate an essay**
   - Enter your essay topic
   - Specify the desired word count
   - Select the language
   - Click "Submit" and watch your essay being generated!

3. **Copy your essay**
   - Use the "📋 Copy Essay" button to copy the generated content

## 📦 Dependencies

```
streamlit
python-dotenv
langchain-groq
langchain-core
langchain-ollama
st-copy-to-clipboard
```

## 🏗️ Project Structure

```
essay-generator/
│
├── app.py              # Main Streamlit application
├── .env                # Environment variables (not tracked in git)
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🤖 Models Used

- **Groq Llama 3.3 70B**: Fast and efficient language model for essay generation
- **DeepSeek V3.1**: Alternative model option (requires Ollama)

## ⚙️ Configuration

You can customize the application by modifying:
- **Temperature**: Adjust creativity (default: 0.7)
- **Model Selection**: Switch between `llm1` (DeepSeek) and `llm2` (Groq) in the code
- **Prompt Template**: Modify the system and human prompts for different essay styles

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure
- Use environment variables for sensitive information

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Yasho**
- GitHub: [@codewithyasho](https://github.com/codewithyasho)

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Groq](https://groq.com/)
- UI created with [Streamlit](https://streamlit.io/)
- DeepSeek model via [Ollama](https://ollama.ai/)

## 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/codewithyasho/essay-generator/issues) on GitHub.

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
