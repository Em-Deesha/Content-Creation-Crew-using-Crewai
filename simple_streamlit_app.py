#!/usr/bin/env python3
"""
Simple Multi-Agent Content Creation System - Streamlit Frontend
================================================================

A clean, simple interface for the CrewAI multi-agent content creation system.
Outputs plain text content without HTML formatting.
"""

import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
from content_creation_team import ContentCreationTeam

# Load environment variables
load_dotenv()

# For Streamlit Cloud deployment, also check secrets
try:
    import streamlit as st
    # Check if running on Streamlit Cloud
    if hasattr(st, 'secrets') and st.secrets:
        # Use secrets from Streamlit Cloud
        os.environ["GOOGLE_API_KEY"] = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
        os.environ["SERPER_API_KEY"] = st.secrets.get("SERPER_API_KEY", os.getenv("SERPER_API_KEY"))
except:
    pass

# Page configuration
st.set_page_config(
    page_title="AI Content Creator",
    page_icon="🤖",
    layout="wide"
)

def main():
    """Main application function."""
    
    # Header
    st.title("🤖 AI Content Creator")
    st.markdown("Multi-Agent AI System for Professional Content Creation")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Status
        google_api = os.getenv("GOOGLE_API_KEY")
        serper_api = os.getenv("SERPER_API_KEY")
        
        if google_api and serper_api:
            st.success("✅ APIs Configured")
        else:
            st.error("❌ API Keys Missing")
        
        st.markdown("---")
        st.markdown("**🤖 AI Agents:**")
        st.markdown("- **Writer**: Creates content")
        st.markdown("- **Editor**: Reviews quality") 
        st.markdown("- **SEO**: Optimizes content")
    
    # Main content form
    st.header("📝 Create Content")
    
    with st.form("content_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input(
                "📌 Topic",
                value="The Future of Artificial Intelligence in Healthcare",
                help="Enter your content topic"
            )
            
            audience = st.text_input(
                "👥 Target Audience", 
                value="healthcare professionals and technology enthusiasts",
                help="Who is your target audience?"
            )
        
        with col2:
            content_type = st.selectbox(
                "📄 Content Type",
                ["blog post", "article", "report", "whitepaper"],
                help="What type of content?"
            )
            
            word_count = st.slider(
                "📊 Word Count",
                min_value=300,
                max_value=3000, 
                value=1000,
                step=100,
                help="Desired word count"
            )
        
        # Submit button
        submitted = st.form_submit_button(
            "🚀 Generate Content",
            use_container_width=True,
            type="primary"
        )
    
    # Process content generation
    if submitted:
        if not google_api or not serper_api:
            st.error("❌ API keys not configured. Please check your .env file.")
            return
        
        # Show progress
        with st.spinner("🤖 AI agents are working..."):
            try:
                # Initialize and run content creation
                team = ContentCreationTeam()
                result = team.create_content(
                    topic=topic,
                    audience=audience,
                    content_type=content_type,
                    word_count=f"{word_count-200}-{word_count+200}"
                )
                
                # Display results
                if result.get("status") == "success":
                    st.success("✅ Content created successfully!")
                    
                    # Show content metadata
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Topic", topic)
                    with col2:
                        st.metric("Audience", audience)
                    with col3:
                        st.metric("Type", content_type)
                    with col4:
                        st.metric("Word Count", word_count)
                    
                    # Display the content
                    st.subheader("📄 Generated Content")
                    
                    # Extract just the content text (remove HTML if present)
                    content = result.get("result", "")
                    
                    # If content contains HTML, extract just the text
                    if "<!DOCTYPE html>" in content or "<html>" in content:
                        # Extract content between <body> tags
                        import re
                        body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
                        if body_match:
                            body_content = body_match.group(1)
                            # Remove HTML tags but keep the text
                            import re
                            clean_content = re.sub(r'<[^>]+>', '', body_content)
                            st.markdown(clean_content)
                        else:
                            st.markdown(content)
                    else:
                        st.markdown(content)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Content",
                        data=content,
                        file_name=f"content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
                    
                else:
                    st.warning("⚠️ Content created in simulation mode")
                    show_simulation_content(topic, audience, content_type, word_count)
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 The system will fall back to simulation mode if APIs are overloaded.")
                show_simulation_content(topic, audience, content_type, word_count)
    
    # Footer
    st.markdown("---")
    st.caption("Powered by CrewAI, Gemini 2.5 Flash, and Serper API")

def show_simulation_content(topic, audience, content_type, word_count):
    """Show simulation content when APIs are not available."""
    
    st.markdown("### 📋 Simulation Mode")
    st.info("Content created in simulation mode (APIs may be overloaded)")
    
    # Simulated content
    simulated_content = f"""
# {topic}

## Introduction

This is a simulated content piece about {topic}, designed for {audience}. 
The content would be structured as a {content_type} with approximately {word_count} words.

## Key Points

- **Point 1**: AI is transforming healthcare through advanced diagnostics
- **Point 2**: Personalized treatment plans are becoming more accessible  
- **Point 3**: Remote monitoring and telemedicine are expanding care access
- **Point 4**: Data-driven insights are improving patient outcomes

## Conclusion

The future of healthcare is being shaped by artificial intelligence, offering 
unprecedented opportunities for {audience} to improve patient care and outcomes.

---

*This is simulated content. For real content generation, ensure your API keys are properly configured.*
    """
    
    st.markdown(simulated_content)
    
    # Download simulated content
    st.download_button(
        label="📥 Download Simulated Content",
        data=simulated_content,
        file_name=f"simulated_content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )

if __name__ == "__main__":
    main()
