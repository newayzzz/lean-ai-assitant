"""
Next-Gen Lean AI Assistant - Main Application
A comprehensive tool for Lean manufacturing framework guidance and implementation.
"""

from ai_providers import get_ai_provider
from config import FRAMEWORKS, INDUSTRY_EXAMPLES, DEFAULT_AI_PROVIDER, APP_NAME, VERSION
from prompts import PromptTemplates
from typing import Optional


class LeanAIAssistant:
    """Main application class for the Lean AI Assistant."""
    
    def __init__(self, ai_provider: str = DEFAULT_AI_PROVIDER):
        """Initialize the assistant with specified AI provider."""
        try:
            self.ai = get_ai_provider(ai_provider)
            self.provider_name = ai_provider
        except Exception as e:
            print(f"⚠️ Error initializing AI provider '{ai_provider}': {e}")
            print("Falling back to ASI1 Mini provider...")
            try:
                self.ai = get_ai_provider("asi1")
                self.provider_name = "asi1"
            except Exception as fallback_error:
                print(f"❌ Fallback failed: {fallback_error}")
                raise RuntimeError("No AI provider available. Please check your API keys.")
    
    def display_welcome(self) -> None:
        """Display welcome message and app info."""
        print(f"\n{'='*60}")
        print(f"🏭 {APP_NAME} v{VERSION}")
        print(f"🤖 Powered by: {self.provider_name.upper()}")
        print(f"{'='*60}")
        print("I'm here to help optimize your factory floor decisions with AI-powered")
        print("guidance on Lean manufacturing frameworks.")
    
    def get_industry_input(self) -> str:
        """Get industry input from user."""
        industry_list = ", ".join(INDUSTRY_EXAMPLES)
        return input(
            f"\nTo tailor this experience, what industry are you in?\n"
            f"Examples: {industry_list}\n"
            f"Your industry: "
        ).strip()
    
    def get_framework_choice(self) -> str:
        """Get framework choice from user."""
        print("\n🔧 Which Lean framework would you like to explore?")
        for key, value in FRAMEWORKS.items():
            print(f"{key}. {value}")
        print("5. Compare frameworks")
        
        return input("Enter choice (1-5): ").strip()
    
    def process_framework_selection(self, choice: str, industry: str) -> tuple[Optional[str], str]:
        """Process framework selection and generate appropriate prompt."""
        if choice == '5':
            prompt = PromptTemplates.framework_comparison(industry)
            return None, prompt
        elif choice in FRAMEWORKS:
            framework = FRAMEWORKS[choice]
            prompt = PromptTemplates.framework_guide(framework, industry)
            return framework, prompt
        else:
            raise ValueError("Invalid framework selection")
    
    def display_response(self, response: str, industry: str) -> None:
        """Display AI response with formatting."""
        print("\n" + "=" * 60)
        header = f"💡 YOUR {industry.upper()} LEAN ROADMAP"
        print(header)
        print("=" * 60)
        print(response)
    
    def handle_follow_up(self, framework: Optional[str], industry: str) -> bool:
        """Handle follow-up interactions. Returns True to continue, False to restart."""
        if not framework:
            return False  # No follow-up for comparison mode
        
        print("\n❓ What would you like to explore next?")
        print("1. Implement in my factory")
        print("2. See AI tools")
        print("3. Restart")
        
        choice = input("Choice: ").strip()
        
        if choice == '1':
            self.show_implementation_plan(framework, industry)
        elif choice == '2':
            self.show_ai_tools(framework, industry)
        elif choice == '3':
            return False  # Signal to restart
        else:
            print("\n⚠️ Invalid selection. Please choose a valid option.")
        
        return True
    
    def show_implementation_plan(self, framework: str, industry: str) -> None:
        """Display implementation roadmap and KPIs."""
        print("\n🚀 Generating custom implementation plan...")
        
        # Get implementation roadmap
        roadmap_prompt = PromptTemplates.implementation_roadmap(framework, industry)
        roadmap = self.ai.call(roadmap_prompt)
        
        print("\n" + "=" * 60)
        print("📝 CUSTOM IMPLEMENTATION ROADMAP")
        print("=" * 60)
        print(roadmap)
        
        # Get KPIs
        kpi_prompt = PromptTemplates.kpi_metrics(framework, industry)
        kpis = self.ai.call(kpi_prompt)
        
        print("\n🎯 KEY PERFORMANCE INDICATORS")
        print("=" * 40)
        print(kpis)
        
        input("\nPress Enter to continue...")
    
    def show_ai_tools(self, framework: str, industry: str) -> None:
        """Display AI tools recommendations and crisis communication integration."""
        print("\n🤖 Curating AI solutions...")
        
        # Get AI tools recommendations
        tools_prompt = PromptTemplates.ai_tools_recommendation(framework, industry)
        tools = self.ai.call(tools_prompt)
        
        print("\n" + "=" * 60)
        print("🛠️ AI TOOLKIT FOR LEAN IMPLEMENTATION")
        print("=" * 60)
        print(tools)
        
        # Get crisis communication integration
        crisis_prompt = PromptTemplates.crisis_communication_integration()
        crisis_info = self.ai.call(crisis_prompt)
        
        print("\n🚨 CRISIS COMMUNICATION INTEGRATION")
        print("=" * 45)
        print(crisis_info)
        
        input("\nPress Enter to continue...")
    
    def run(self) -> None:
        """Main application loop."""
        while True:
            try:
                self.display_welcome()
                
                # Get user inputs
                industry = self.get_industry_input()
                if not industry:
                    print("⚠️ Industry is required. Please try again.")
                    continue
                
                framework_choice = self.get_framework_choice()
                
                print("\n🤖 Analyzing your selection...")
                
                # Process selection and get AI response
                selected_framework, prompt = self.process_framework_selection(framework_choice, industry)
                response = self.ai.call(prompt)
                
                # Display response
                self.display_response(response, industry)
                
                # Handle follow-up interactions
                while True:
                    if not self.handle_follow_up(selected_framework, industry):
                        break  # Break inner loop to restart
                    
                    # Continue follow-up loop
                    continue
                
            except KeyboardInterrupt:
                print("\n\n👋 Thank you for using the Lean AI Assistant!")
                break
            except ValueError as e:
                print(f"\n⚠️ {e} Please choose a number between 1 and 5.")
                continue
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                print("Please try again or contact support.")
                continue


def main():
    """Entry point for the application."""
    import sys
    
    # Allow provider selection via command line argument
    provider = DEFAULT_AI_PROVIDER
    if len(sys.argv) > 1:
        provider = sys.argv[1]
    
    try:
        assistant = LeanAIAssistant(provider)
        assistant.run()
    except Exception as e:
        print(f"❌ Failed to start application: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check your API keys in .env file")
        print("2. Ensure you have internet connectivity")
        print("3. Verify your API quotas/limits")
        sys.exit(1)


if __name__ == "__main__":
    main()