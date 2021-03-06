import discord

import os
import random

from util import reddit


async def send_random_meme(ctx, subreddit):
    meme = random.choice(os.listdir(f'submissions/{subreddit}'))
    meme_id = meme[:-4]
    meme_ext = meme[-4:]
    title, link, score, comments = await reddit.get_info(meme_id)

    im = discord.File(
        f'submissions/{subreddit}/{meme}', filename=f'meme{meme_ext}')
    embed = discord.Embed()
    embed.title = title
    embed.url = f'https://www.reddit.com{link}'
    embed.set_image(url=f'attachment://meme{meme_ext}')
    embed.set_footer(text=f'{score} upvotes, {comments} comments')
    await ctx.send(file=im, embed=embed)
