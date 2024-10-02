import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext,WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero,  cartesia


load_dotenv()

async def entry(ctx: JobContext):
    chat_ctx = llm.ChatContext().append(
        role="system",
        text=("你是一个说中文的，并且说话简洁的助手。")
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    asssitant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(language="zh"),
        tts=cartesia.TTS(
            model="sonic-multilingual",
            language="zh",
            voice="e90c6678-f0d3-4767-9883-5d0ecf5894a8", #Chinese Female Conversational
            api_key="xxxxx" #replaced with your own api key
            ),
        llm=openai.LLM.with_ollama(base_url="http://localhost:11434/v1", model="aispin/qwen2.5-7b-instruct-abliterated-v2.q4_k_s.gguf:latest"),
        chat_ctx=chat_ctx
    )
    asssitant.start(ctx.room)

    await asyncio.sleep(1)
    await asssitant.say("你好，我是小姐姐，很高兴见到你",allow_interruptions=False)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entry))