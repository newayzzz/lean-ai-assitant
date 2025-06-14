from ai import call_gpt

"""
We are creating a detailed prompt for an interactive Lean+SixSigma chatbot prototype.
The goal is to guide factory floor decision-making by:
    1. Identifying the user's industry,
    2. Choosing their framework of interest (TPS, FPS, SPW, LSS),
    3. Providing an interactive explanation of the chosen framework.
"""

def main():
    industry_identification = input(
        "🏭 Welcome to the Next-Gen Lean AI Assistant! I'm here to help optimize your factory floor decisions.\n"
        "To tailor this experience, what industry are you in? Examples:\n"
        "- Automotive, Electronics, Pharmaceuticals, Mining & Metals,\n"
        "- Aerospace, Food Processing, Textile/Apparel, Medical Devices,\n"
        "- Consumer Goods, Renewable Energy, Biotech, Construction Materials,\n"
        "- Chemicals, Plastics & Composites, Agriculture Equipment,\n"
        "- Defense Manufacturing, Industrial Machinery, or something else?\n"
        "Your industry: "
    )

    framework_choice = input(
        "\n🔧 Thank you. Which Lean framework would you like to explore?\n"
        "1. TPS - Toyota Production System\n"
        "2. FPS - Ford Production System\n"
        "3. SPW - Stellantis Production Way\n"
        "4. LSS - Lean Six Sigma\n"
        "5. Compare frameworks\n"
        "Enter choice (1-5): "
    )

    print("\n🤖 Analyzing your selection...")

    frameworks = {
        '1': 'Toyota Production System (TPS)',
        '2': 'Ford Production System (FPS)',
        '3': 'Stellantis Production Way (SPW)',
        '4': 'Lean Six Sigma (LSS)'
    }

    # Build the prompt based on selection
    if framework_choice == '5':
        prompt = (
            f"Compare Toyota Production System (TPS), Ford Production System (FPS), "
            f"Stellantis Production Way (SPW), and Lean Six Sigma highlighting:\n"
            f"- Core principles and differences\n"
            f"- Best-fit industries (especially {industry_identification})\n"
            f"- AI integration opportunities\n"
            f"- Real-world Canadian examples where relevant\n"
            f"Structure: Concise comparison table then 2-sentence summary per framework."
        )
        selected_framework = None

    elif framework_choice in frameworks:
        selected_framework = frameworks[framework_choice]
        prompt = (
            f"Create interactive guide for {selected_framework} in the {industry_identification} industry covering:\n"
            f"1. Core principles (max 3 key concepts)\n"
            f"2. Industry-specific implementation roadmap\n"
            f"3. AI integration opportunities (reference Toyota/HBR examples)\n"
            f"4. Canadian case study example\n"
            f"5. Interactive options: 'Dive deeper into [concept]', 'See simulation', 'Compare frameworks'\n"
            f"Format: Conversational tone with emoji section breaks 🇨🇦"
        )
    else:
        print("\n⚠️ Invalid framework selection. Please choose a number between 1 and 5.")
        return

    # Generate and display response
    response = call_gpt(prompt)
    print("\n" + "=" * 50)
    header = f"💡 YOUR {industry_identification.upper()} LEAN ROADMAP"
    print(header)
    print("=" * 50)
    print(response)

    # Follow-up interaction loop
    while True:
        follow_up = input(
            "\n❓ What would you like to explore next?\n"
            "1. Implement in my factory\n"
            "2. See AI tools\n"
            "3. Restart\n"
            "Choice: "
        )

        if follow_up == '1' and selected_framework:
            print("\n🚀 Generating custom implementation plan...")
            implementation_prompt = (
                f"Create a 6-month implementation roadmap for {selected_framework} in the {industry_identification} industry with Canadian context:\n"
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
            implementation_plan = call_gpt(implementation_prompt)
            print("\n" + "=" * 50)
            print("📝 CUSTOM IMPLEMENTATION ROADMAP")
            print("=" * 50)
            print(implementation_plan)

            kpi_prompt = (
                f"Create 5 SMART KPIs for {selected_framework} implementation in Canadian {industry_identification} sector with AI integration targets"
            )
            kpis = call_gpt(kpi_prompt)
            print("\n🎯 KEY PERFORMANCE INDICATORS")
            print(kpis)
            input("\nPress Enter to continue...")

        elif follow_up == '2' and selected_framework:
            print("\n🤖 Curating AI solutions...")
            ai_prompt = (
                f"Recommend AI tools for {selected_framework} implementation in {industry_identification} with Canadian availability:\n"
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
            ai_tools = call_gpt(ai_prompt)
            print("\n" + "=" * 50)
            print("🛠️ AI TOOLKIT FOR LEAN IMPLEMENTATION")
            print("=" * 50)
            print(ai_tools)

            crisis_prompt = (
                "Integrate crisis communication features from knowledge graph:\n"
                "1. Two-way communication alerts\n"
                "2. Emergency Operations protocols\n"
                "3. Business crisis communication templates\n"
                "Show how these interface with Lean AI systems"
            )
            crisis_integration = call_gpt(crisis_prompt)
            print("\n🚨 CRISIS COMMUNICATION INTEGRATION")
            print(crisis_integration)

        elif follow_up == '3':
            print("\n🔄 Restarting session...")
            main()
            return

        else:
            print("\n⚠️ Invalid selection or no framework chosen. Please choose a valid option.")
            continue


if __name__ == "__main__":
    main()
