import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext,WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero


load_dotenv()

async def entry(ctx: JobContext):
    chat_ctx = llm.ChatContext().append(
        role="system",
        text=("你是一个善解人意的女孩子，你用温柔的可以融化坚冰的语气说话。")
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    asssitant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        tts=openai.TTS(voice="nova"),
        llm=openai.LLM(model="gpt-4o-mini"),
        chat_ctx=chat_ctx
    )
    asssitant.start(ctx.room)

    await asyncio.sleep(1)
    await asssitant.say("你好，我是小姐姐，很高兴见到你",allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entry))