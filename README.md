# Story2Hallucination

This is a Colab notebook used to render paragraphs and whole stories of text as animations using [Big Sleep](https://github.com/lucidrains/big-sleep/).  The animations from the stories look wild, hence, Story2Hallucination.

[![A hallucinated animated of a.ttent.io/n](story2halluc.gif)](https://www.youtube.com/watch?v=9Y-UZquQDf0)

The [main notebook](https://github.com/lots-of-things/Story2Hallucination/blob/main/Story2Hallucination.ipynb) runs on Colab and generates raw images and saves them to drive so you can download and create longer videos.  There is also a [GIF making notebook](https://github.com/lots-of-things/Story2Hallucination/blob/main/Story2Hallucination_GIF.ipynb) that will make a GIF on colab that you can display or download directly without connecting to Drive (but note that large gifs won't play on colab and will take a long time to download).


You can easily open the notebook in Google Colab here.

[![Open In Colab][colab-badge]][colab-notebook]

[colab-notebook]: <https://colab.research.google.com/drive/1cCo7z-HaoiUCqvPJJTjczmJl-_iWCcCl?usp=sharing>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>

For more info please see the [Big Sleep repo](https://github.com/lucidrains/big-sleep/) and [this blog post](https://bonkerfield.org/2021/01/story2hallucination/).

To render the story audio you can use Google's TTS API. More info [here](https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3)

Credits:
Credit to [Phil Wang](https://github.com/lucidrains/) and [Ryan Murdock](https://rynmurdock.github.io/) for making the Big Sleep, and [@HoverSquid](https://www.twitch.tv/hoversquid) for fixing up the notebook, adding features, and upgrading the BigSleep version Check out [@HoverSquid's Twitch Stream](https://www.twitch.tv/hoversquid) to see Story2Hallucination animate AI Dungeon games.


