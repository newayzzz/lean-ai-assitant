"""
Prompt templates for different types of AI interactions.

Created by: Saqeb Newaz
"""

from typing import Optional


class PromptTemplates:
    """Collection of prompt templates for the Lean AI Assistant."""
    
    @staticmethod
    def framework_comparison(industry: str) -> str:
        """Generate prompt for comparing all frameworks."""
        return (
            f"Compare Toyota Production System (TPS), Ford Production System (FPS), "
            f"Stellantis Production Way (SPW), and Lean Six Sigma highlighting:\n"
            f"- Core principles and differences\n"
            f"- Best-fit industries (especially {industry})\n"
            f"- AI integration opportunities\n"
            f"- Real-world Canadian examples where relevant\n"
            f"Structure: Concise comparison table then 2-sentence summary per framework."
        )
    
    @staticmethod
    def framework_guide(framework: str, industry: str) -> str:
        """Generate prompt for interactive framework guide."""
        return (
            f"Create interactive guide for {framework} in the {industry} industry covering:\n"
            f"1. Core principles (max 3 key concepts)\n"
            f"2. Industry-specific implementation roadmap\n"
            f"3. AI integration opportunities (reference Toyota/HBR examples)\n"
            f"4. Canadian case study example\n"
            f"5. Interactive options: 'Dive deeper into [concept]', 'See simulation', 'Compare frameworks'\n"
            f"Format: Conversational tone with emoji section breaks 🇨🇦"
        )
    
    @staticmethod
    def implementation_roadmap(framework: str, industry: str) -> str:
        """Generate prompt for 6-month implementation roadmap."""
        return (
            f"Create a 6-month implementation roadmap for {framework} in the {industry} industry with Canadian context:\n"
            "1. **Phase 1: Assessment (Month 1)**\n"
            "   - Current state value stream mapping\n"
            "   - Waste identification (7+1 wastes)\n"
            "   - Canadian regulatory compliance checklist\n"
            "2. **Phase 2: Pilot Design (Month 2)**\n"
            "   - Select 3 high-impact processes for Kaizen events\n"
            "   - AI integration opportunities assessment\n"
            "   - Cross-functional team formation\n"
            "3. **Phase 3: Execution (Months 3-4)**\n"
            "   - Standardized work documentation\n"
            "   - Visual management system setup\n"
            "   - AI-powered real-time monitoring\n"
            "4. **Phase 4: Scale & Sustain (Months 5-6)**\n"
            "   - Full deployment across production lines\n"
            "   - Digital Andon system implementation\n"
            "   - Continuous improvement cadence\n"
            "Include Canadian-specific:\n"
            "- Supply chain considerations\n"
            "- Labor regulations\n"
            "- Climate impact mitigation"
        )
    
    @staticmethod
    def kpi_metrics(framework: str, industry: str) -> str:
        """Generate prompt for SMART KPIs."""
        return (
            f"Create 5 SMART KPIs for {framework} implementation in Canadian {industry} "
            f"sector with AI integration targets. Include baseline, target, and measurement frequency."
        )
    
    @staticmethod
    def ai_tools_recommendation(framework: str, industry: str) -> str:
        """Generate prompt for AI tools recommendation."""
        return (
            f"Recommend AI tools for {framework} implementation in {industry} with Canadian availability:\n"
            "1. **Predictive Maintenance** (2 tools with pricing)\n"
            "2. **Quality Control** (2 computer vision solutions)\n"
            "3. **Supply Chain Optimization** (1 Canadian-specific platform)\n"
            "4. **Real-time Analytics** (1 edge computing solution)\n"
            "For each:\n"
            "- Vendor name & Canadian availability\n"
            "- Integration requirements\n"
            "- ROI case study summary\n"
            "- Free trial information"
        )
    
    @staticmethod
    def crisis_communication_integration() -> str:
        """Generate prompt for crisis communication features."""
        return (
            "Integrate crisis communication features from knowledge graph:\n"
            "1. Two-way communication alerts\n"
            "2. Emergency Operations protocols\n"
            "3. Business crisis communication templates\n"
            "Show how these interface with Lean AI systems for manufacturing environments."
        )