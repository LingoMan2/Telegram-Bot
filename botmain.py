# Importing load_dotenv package to access bot token
from dotenv import load_dotenv
import os
# Importing Python-Telegram-Bot package to build bot
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler, CallbackContext, filters


# Load Env
load_dotenv()

async def CheckUserIsMember(UserID, update, context):
    # Some Information About Channels And User
    MainChannelID = -1002144403590
    SecondChannel = -1001950587974
    ThirdChannelID = -1001854426257
    User_ID = UserID

    # Check If The User Is Member Of These Channels
    MainChannel_IsMember = await context.bot.getChatMember(MainChannelID, User_ID)
    ChatGroup_IsMember = await context.bot.getChatMember(SecondChannel, User_ID)
    ThirdChannel_IsMember = await context.bot.getChatMember(ThirdChannelID, User_ID)

    # Return Member Status As A Object 
    IsMember = {
        "MainChannel": {
            "status": MainChannel_IsMember.status
        },
        "Chat_Group": {
            "status": ChatGroup_IsMember.status
        },
        "Third_Channel": {
            "status": ThirdChannel_IsMember.status
        }
    }

    return IsMember




# Handle Start Message
async def StartMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Calling Function To Check If User Joined To Our Channels Or Not
    IsMemberOfChannels = await CheckUserIsMember(update.message.from_user.id, update=update, context=context)



    # Channel Links To Send To User To Join Them
    Main_Channel = "https://t.me/mrabasincome"
    Chat_Link = "https://t.me/ddidoudd"
    Third_Channel = "https://t.me/mrabas_chat"
    Youtube_Link = "https://youtube.com/@mrabasincome?si=v3KoWKRHW4qPm2EW"

    # InlineKeyboardMarkup For Links And Check If User Is Member Of Channels
    Links_InlineMarkUp = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Link1", url=Main_Channel)],
        [InlineKeyboardButton(text="Link2", url=Chat_Link)],
        [InlineKeyboardButton(text="Link3", url=Third_Channel)],
        [InlineKeyboardButton(text="Subscribe Youtube", url=Youtube_Link)],
        [InlineKeyboardButton(text="✅ تایید", callback_data="verify_join")],
    ])


    # If Chat Is In Private
    if update.message.chat.type == "private":
        # If User Is Member Of Channels
        if IsMemberOfChannels["MainChannel"]['status'] == "member" and IsMemberOfChannels["Chat_Group"]['status'] == "member" and IsMemberOfChannels["Third_Channel"]['status'] == "member":
            # Send Message To User
            await context.bot.send_message(
                chat_id = update.message.chat_id,
                reply_to_message_id = update.message.id,
                text="لینک سایت 👇👇👇\nhttps://zefoy.com\nبرای حل مشکل هم به گروه چت پیام بدین"
            )
        # Check If User Is Creator Or Not
        elif IsMemberOfChannels["MainChannel"]['status'] == "creator" and IsMemberOfChannels["Chat_Group"]['status'] == "creator" and IsMemberOfChannels["Third_Channel"]['status'] == "creator":
            await context.bot.send_message(
                chat_id = update.message.chat_id,
                reply_to_message_id = update.message.id,
                text="لینک سایت 👇👇👇\nhttps://zefoy.com\nبرای حل مشکل هم به گروه چت پیام بدین"
            )
        else:
            # Send Channel Links To User
            await context.bot.send_message(
                chat_id = update.message.chat_id,
                reply_to_message_id = update.message.id,
                text="برای استفاده از ربات ابتدا در چنل های زیر عضو شوید سپس بر روی گزینه ✅ تایید ضربه بزنید",
                parse_mode="MarkdownV2",
                reply_markup=Links_InlineMarkUp,
            )


# Handle CallBackQuery
async def CallBackHandler(update: Update, context: CallbackContext):
    # Delete Previus Message And Check Again
    await context.bot.deleteMessage(
        message_id = update.callback_query.message.id,
        chat_id = update.callback_query.message.chat.id
    )
    # Getting Information That User Has Joined To Our Channel Or Not
    IsMemberOfChannels = await CheckUserIsMember(update.callback_query.message.chat.id, update=update, context=context)


    # Channel Links To Send To User To Join Them
    Main_Channel = "https://t.me/mrabasincome"
    Chat_Link = "https://t.me/ddidoudd"
    Third_Channel = "https://t.me/mrabas_chat"
    Youtube_Link = "https://youtube.com/@mrabasincome?si=v3KoWKRHW4qPm2EW"

    # InlineKeyboardMarkup For Links And Check If User Is Member Of Channels
    Links_InlineMarkUp = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Link1", url=Main_Channel)],
        [InlineKeyboardButton(text="Link2", url=Chat_Link)],
        [InlineKeyboardButton(text="Link3", url=Third_Channel)],
        [InlineKeyboardButton(text="Subscribe Youtube", url=Youtube_Link)],
        [InlineKeyboardButton(text="✅ تایید", callback_data="verify_join")],
    ])


    # If Chat Is In Private
    if update.callback_query.message.chat.type == "private":
        # If User Is Member Of Channels
        if IsMemberOfChannels["MainChannel"]['status'] == "member" and IsMemberOfChannels["Chat_Group"]['status'] == "member" and IsMemberOfChannels["Third_Channel"]['status'] == "member":
            # Send Message To User
            await context.bot.send_message(
                chat_id = update.callback_query.message.chat_id,
                text="لینک سایت 👇👇👇\nhttps://zefoy.com\nبرای حل مشکل هم به گروه چت پیام بدین"
            )
            await update.callback_query.answer()
        # Check If User Is Creator
        elif IsMemberOfChannels["MainChannel"]['status'] == "creator" and IsMemberOfChannels["Chat_Group"]['status'] == "creator" and IsMemberOfChannels["Third_Channel"]['status'] == "creator":
            # Send Message To User
            await context.bot.send_message(
                chat_id = update.callback_query.message.chat_id,
                reply_to_message_id = update.callback_query.message.id,
                text="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://zefoy.com/&ved=2ahUKEwi_lKuytbqFAxW-GhAIHaBsATcQFnoECAUQAQ&usg=AOvVaw1MzXYGSfQjjNcK7vePDsI8"
            )
            await update.callback_query.answer()
        else:
            # Send Channel Links To User
            await context.bot.send_message(
                chat_id = update.callback_query.message.chat_id,
                text="برای استفاده از ربات ابتدا در چنل های زیر عضو شوید سپس بر روی گزینه ✅ تایید ضربه بزنید",
                parse_mode="MarkdownV2",
                reply_markup=Links_InlineMarkUp,
            )
            # Answer CallBack Request
            await update.callback_query.answer()
    else:
        # Answer CallBack Request
        await update.callback_query.answer()


# Start Bot
if __name__ == "__main__":
    # Build And Setup Bot With Token
    Bot = ApplicationBuilder().token(os.getenv('API_TOKEN')).build()

    # Adding Command Handlers
    StartCommand = CommandHandler('start', StartMessage)
    Bot.add_handler(StartCommand)
    Bot.add_handler(CallbackQueryHandler(CallBackHandler))

    # Running Bot
    Bot.run_polling()