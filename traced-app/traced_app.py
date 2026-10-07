from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "In one sentence, what is the capital of Japan?",
    (
        "Summarize the following paragraph in three concise bullet points. "
        "Keep the important facts and avoid adding information:\n\n"
        "A community garden was started by local residents on an unused city lot. "
        "Volunteers grow seasonal vegetables, share them with nearby families, "
        "and teach children about composting. The city provides water access, "
        "while a neighborhood group coordinates weekly work sessions."
    ),
    (
        "Analyze this hypothetical decision for a small neighborhood library: "
        "Should it extend its opening hours by two evenings per week? Consider "
        "potential benefits for students and working adults, staffing and utility "
        "costs, safety, and how the library could test the idea before making it "
        "permanent. Give a balanced recommendation with supporting reasons, "
        "assumptions, and one practical way to measure success."
    ),
]

for i, prompt in enumerate(prompts, start=1):
    response = llm.invoke(prompt)
    print(f"\n--- Response {i} ---")
    print(response.content)