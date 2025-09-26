# 🚀 Multi-Agent Content Creation System

A sophisticated AI-powered content creation system that uses multiple specialized agents to generate high-quality, SEO-optimized content. Built with CrewAI, Gemini 2.5 Flash, and Serper API.

## ✨ Features

- **🤖 Multi-Agent Architecture**: Three specialized AI agents working together
- **📝 Content Creation**: Generate engaging, well-structured content on any topic
- **🔍 SEO Optimization**: Built-in SEO optimization for better search visibility
- **🌐 Web Research**: Real-time web research using Serper API
- **✨ Professional Quality**: Editor agent ensures high-quality output
- **💻 Web Interface**: Beautiful Streamlit frontend for easy use
- **📱 Responsive Design**: Works on desktop, tablet, and mobile

## 🤖 AI Agents

### 1. 📝 Content Writer
- **Role**: Creates engaging, original content
- **Skills**: Research, writing, content structuring
- **Tools**: Web search, content generation
- **Output**: Well-researched, structured content

### 2. ✏️ Content Editor
- **Role**: Reviews and improves content quality
- **Skills**: Grammar, style, fact-checking, brand consistency
- **Tools**: Content analysis, editing
- **Output**: Polished, error-free content

### 3. 🔍 SEO Specialist
- **Role**: Optimizes content for search engines
- **Skills**: Keyword research, SEO optimization, social media snippets
- **Tools**: Web search, SEO analysis
- **Output**: SEO-optimized content with social media snippets

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Serper API key

### Quick Setup
```bash
# 1. Clone the repository
git clone <your-repo-url>
cd Multi-Agent-Content-Creation

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with your API keys
echo "GOOGLE_API_KEY=your_gemini_api_key_here" > .env
echo "SERPER_API_KEY=your_serper_api_key_here" >> .env
```

## 🚀 Usage

### Web Interface (Recommended)
```bash
# Run the Streamlit application
streamlit run simple_streamlit_app.py
```
Then open your browser to `http://localhost:8501`

### Python API
```python
from content_creation_team import ContentCreationTeam

# Initialize the team
team = ContentCreationTeam()

# Create content
result = team.create_content(
    topic="The Future of Artificial Intelligence",
    audience="technology enthusiasts",
    content_type="blog post",
    word_count="1000-1200"
)

print(result)
```

## 📁 Project Structure

```
├── content_creation_team.py    # Core multi-agent system
├── simple_streamlit_app.py    # Simple web interface (recommended)
├── new_streamlit_app.py       # Advanced web interface with HTML output
├── requirements.txt           # Dependencies
├── launch_app.py             # Launch script
├── README.md                  # Documentation
└── .env                       # API keys (create this)
```

## 🔧 Configuration

### API Keys Setup
1. **Google Gemini API**: 
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a new project
   - Generate an API key
   - Add to your `.env` file

2. **Serper API**:
   - Visit [Serper.dev](https://serper.dev/)
   - Sign up for a free account
   - Get your API key
   - Add to your `.env` file

### Environment Variables
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

## 🎯 Features

### Content Creation
- **🔍 Research-Driven**: Uses web search for current information
- **👥 Audience-Tailored**: Content customized for specific audiences
- **📈 SEO-Optimized**: Built-in search engine optimization
- **✨ Professional Quality**: Editor agent ensures high standards
- **📱 Multiple Formats**: Blog posts, articles, reports, whitepapers

### Multi-Agent Workflow
1. **📝 Writer Agent**: Researches and creates initial content
2. **✏️ Editor Agent**: Reviews and improves content quality
3. **🔍 SEO Agent**: Optimizes for search engines and social media

### Web Interface
- **🎨 Simple Interface**: Clean, user-friendly design
- **⏱️ Real-time Progress**: See agents working in real-time
- **👀 Content Preview**: View generated content before downloading
- **💾 Download Options**: Save content in various formats
- **📊 Progress Tracking**: Monitor content generation progress

## 🚀 Deployment

### Local Development
```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
streamlit run simple_streamlit_app.py
```

### Production Deployment
1. **Streamlit Cloud**: 
   - Connect your GitHub repository
   - Deploy with one click
   - Free hosting available

2. **Heroku**: 
   - Use the provided Procfile
   - Free tier available

3. **Railway**: 
   - Deploy with one click
   - Free tier available

4. **Render**: 
   - Connect your repository
   - Free tier available

## 📊 Performance

### System Requirements
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB for dependencies
- **Network**: Stable internet for API calls
- **Python**: 3.8 or higher

### API Limits
- **Gemini Free Tier**: 50 requests per day
- **Serper Free Tier**: 2,500 searches per month
- **Upgrade**: For higher limits, upgrade your API plans

## 🔍 Troubleshooting

### Common Issues
1. **API Key Errors**: 
   - Check your `.env` file
   - Verify API keys are correct
   - Ensure keys are active

2. **Import Errors**: 
   - Ensure all dependencies are installed
   - Run `pip install -r requirements.txt`

3. **Rate Limits**: 
   - Wait for quota reset (24 hours)
   - Upgrade your API plan
   - Use simulation mode

4. **Memory Issues**: 
   - Increase system RAM
   - Use smaller models
   - Close other applications

### Debug Mode
```bash
streamlit run simple_streamlit_app.py --logger.level debug
```

## 📈 Future Enhancements

- [ ] Support for more LLM providers (OpenAI, Claude, etc.)
- [ ] Advanced content templates
- [ ] Batch content generation
- [ ] Content analytics dashboard
- [ ] Multi-language support
- [ ] Content scheduling
- [ ] Team collaboration features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the error messages
3. Verify your API configuration
4. Test with the quick actions in the sidebar
5. Create an issue on GitHub

## 🎉 Success Stories

- **Content Marketing**: Generate blog posts for your website
- **SEO Optimization**: Create SEO-friendly content
- **Social Media**: Generate social media snippets
- **Research**: Get well-researched content on any topic
- **Professional Writing**: Create reports, whitepapers, and articles

---

**Powered by CrewAI, Gemini 2.5 Flash, and Serper API** 🚀

**Ready to create amazing content? Start your multi-agent system today!** ✨