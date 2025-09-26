#!/usr/bin/env python3
"""
Advanced Multi-Agent Content Creation System - Streamlit Frontend
================================================================

A modern, interactive web interface for the CrewAI multi-agent content creation system.
Features real-time content generation, progress tracking, and comprehensive output display.
"""

import streamlit as st
import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from content_creation_team import ContentCreationTeam

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Content Creation Studio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .success-card {
        background: #d4edda;
        border-left: 4px solid #28a745;
    }
    .warning-card {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
    }
    .error-card {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function."""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 AI Content Creation Studio</h1>
        <p>Multi-Agent AI System for Professional Content Creation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Status
        st.subheader("🔑 API Status")
        google_api = os.getenv("GOOGLE_API_KEY")
        serper_api = os.getenv("SERPER_API_KEY")
        
        if google_api and serper_api:
            st.success("✅ All APIs Configured")
            st.info("Using environment variables")
        else:
            st.error("❌ API Keys Missing")
            st.warning("Please configure your API keys in the .env file")
        
        # System Status
        st.subheader("📊 System Status")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gemini API", "✅ Active" if google_api else "❌ Inactive")
        with col2:
            st.metric("Serper API", "✅ Active" if serper_api else "❌ Inactive")
        
        # Agent Information
        st.subheader("🤖 AI Agents")
        st.markdown("""
        **Writer Agent**
        - Creates engaging content
        - Researches topics
        - Structures information
        
        **Editor Agent**
        - Reviews quality
        - Improves readability
        - Ensures consistency
        
        **SEO Agent**
        - Optimizes for search
        - Adds keywords
        - Creates social snippets
        """)
        
        # Quick Actions
        st.subheader("🎯 Quick Actions")
        if st.button("🔄 Test System", help="Test the multi-agent system"):
            test_system()
        
        if st.button("📊 View Statistics", help="View system statistics"):
            show_statistics()
    
    # Main content area
    st.header("📝 Content Creation Studio")
    
    # Content form
    with st.form("content_form"):
        st.subheader("Content Requirements")
        
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input(
                "📌 Topic",
                value="The Future of Artificial Intelligence in Healthcare",
                help="Enter the main topic for your content"
            )
            
            audience = st.text_input(
                "👥 Target Audience",
                value="healthcare professionals and technology enthusiasts",
                help="Who is your target audience?"
            )
        
        with col2:
            content_type = st.selectbox(
                "📄 Content Type",
                ["blog post", "article", "report", "whitepaper", "social media post", "email newsletter"],
                help="What type of content do you want to create?"
            )
            
            word_count = st.slider(
                "📊 Word Count",
                min_value=300,
                max_value=3000,
                value=1000,
                step=100,
                help="Desired word count for your content"
            )
        
        # Advanced options
        with st.expander("🔧 Advanced Options"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                research_depth = st.selectbox(
                    "Research Depth",
                    ["Basic", "Comprehensive", "In-depth"],
                    index=1
                )
            
            with col2:
                tone = st.selectbox(
                    "Content Tone",
                    ["Professional", "Casual", "Academic", "Conversational"],
                    index=0
                )
            
            with col3:
                seo_focus = st.selectbox(
                    "SEO Focus",
                    ["Low", "Medium", "High"],
                    index=1
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
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Initialize content creation team
            status_text.text("🤖 Initializing AI agents...")
            progress_bar.progress(10)
            
            team = ContentCreationTeam()
            
            # Generate content
            status_text.text("📝 Creating content...")
            progress_bar.progress(30)
            
            result = team.create_content(
                topic=topic,
                audience=audience,
                content_type=content_type,
                word_count=f"{word_count-200}-{word_count+200}"
            )
            
            progress_bar.progress(80)
            status_text.text("✨ Finalizing content...")
            
            # Display results
            display_results(result, topic, audience, content_type, word_count)
            
            progress_bar.progress(100)
            status_text.text("✅ Content generation complete!")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 The system will fall back to simulation mode if APIs are overloaded.")
            
            # Show simulation mode
            show_simulation_mode(topic, audience, content_type, word_count)
    
    # Footer
    st.markdown("---")
    st.markdown("### 🚀 Deploy Your Own Instance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Streamlit Cloud**")
        st.markdown("Deploy directly from GitHub")
    
    with col2:
        st.markdown("**Heroku**")
        st.markdown("Free tier available")
    
    with col3:
        st.markdown("**Railway**")
        st.markdown("Free tier available")
    
    with col4:
        st.markdown("**Render**")
        st.markdown("Free tier available")
    
    st.markdown("---")
    st.caption("Powered by CrewAI, Gemini 2.5 Flash, and Serper API")

def display_results(result, topic, audience, content_type, word_count):
    """Display the content generation results."""
    
    if result.get("status") == "success":
        st.success("🎉 Content created successfully!")
        
        # Content metadata
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Topic", topic)
        with col2:
            st.metric("Audience", audience)
        with col3:
            st.metric("Type", content_type)
        with col4:
            st.metric("Word Count", word_count)
        
        # Display content
        st.subheader("📄 Generated Content")
        st.markdown(result.get("result", "No content generated"))
        
        # Download button
        content_text = str(result.get("result", ""))
        st.download_button(
            label="📥 Download Content",
            data=content_text,
            file_name=f"content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
        
    else:
        st.warning("⚠️ Content created in simulation mode")
        show_simulation_mode(topic, audience, content_type, word_count)

def show_simulation_mode(topic, audience, content_type, word_count):
    """Show simulation mode when APIs are not available."""
    
    st.markdown("### 📋 Content Simulation")
    st.info("Content created in simulation mode (APIs may be overloaded)")
    
    # Workflow steps
    st.markdown("**Workflow:**")
    st.markdown("""
    • **Writer Agent** creates content (Gemini 2.5 Flash + Serper)
    • **Editor Agent** reviews and improves (Gemini 2.5 Flash)
    • **SEO Agent** optimizes for search engines (Gemini 2.5 Flash + Serper)
    """)
    
    # Content metadata
    st.markdown("**Content Metadata:**")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Topic", topic)
    with col2:
        st.metric("Audience", audience)
    with col3:
        st.metric("Type", content_type)
    with col4:
        st.metric("Word Count", word_count)
    
    # Simulated content
    st.markdown("### 📄 Simulated Content")
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

def test_system():
    """Test the multi-agent system."""
    with st.spinner("Testing system..."):
        try:
            team = ContentCreationTeam()
            result = team.create_content(
                topic="Test Topic",
                audience="test audience",
                content_type="blog post",
                word_count="500-600"
            )
            
            if result.get("status") == "success":
                st.success("✅ System test successful!")
            else:
                st.warning("⚠️ System test completed in simulation mode")
                
        except Exception as e:
            st.error(f"❌ System test failed: {str(e)}")

def show_statistics():
    """Show system statistics."""
    st.subheader("📊 System Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Sessions", "1")
    with col2:
        st.metric("Content Generated", "1")
    with col3:
        st.metric("Success Rate", "100%")

if __name__ == "__main__":
    main()
