from pyrogram import Client, filters
from pyrogram.types import Message


shell_usage = f"**USAGE:** Executes terminal commands directly via bot.\n\n<pre>/shell pip install requests</pre>"

@Client.on_message(filters.command(["shell"]))
async def shell(client: Client, message: Message):
    """
    Executes terminal commands via bot.
    """
    if not one(message.from_user.id):
        return

    if len(message.command) < 2:
        return await message.reply_text(shell_usage, quote=True)

    user_input = message.text.split(None, 1)[1].split(" ")

    try:
        shell = subprocess.Popen(
            user_input, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        stdout, stderr = shell.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    except Exception as error:
        return await message.reply_text(f"**Error**:\n\n{error}", quote=True)

    if len(result) > 2000:
        file = BytesIO(result.encode())
        file.name = "output.txt"
        await message.reply_text("Output is too large (Sending it as File)", quote=True)
        await client.send_document(message.chat.id, file, caption=file.name)
    else:
        await message.reply_text(f"**Output:**:\n\n{result}", quote=True)
