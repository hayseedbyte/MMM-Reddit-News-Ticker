# MMM-Reddit-News-Ticker

This is a module for the [MagicMirror²](https://github.com/MichMich/MagicMirror/).

Looks and acts like the horizontally scrolling newsticker from CNN. By pulling the _top_ 50 submission titles from reddit.com/r/news, it avoids pulling clickbait article titles that don't impart any facts, leveraging the fact that redditors tend to downvote clickbait or sensationalist stories.

![screenshot](/images/screenshot1.png)

## Using the module

Requires [python3](https://www.python.org/downloads/).

You will need to get your own [client ID and secret](https://www.reddit.com/prefs/apps) from reddit.

![reddit api](/images/reddit-api.png)

To use this module, add the following configuration block to the modules array in the `config/config.js` file:

```js
var config = {
  modules: [
    {
      module: 'MMM-Reddit-News-Ticker',
      position: 'bottom_bar'
      config: {
        client_id: 'XXXXXXXXXXXXXXXXXXXX'
        secret: 'XXXXXXXXXXXXXXXXXXXXX'
      },
    },
  ],
};
```

## Configuration options

| Option      | Description                          |
| ----------- | ------------------------------------ |
| `client_id` | _Required_ Your reddit API client id |
| `secret`    | _Required_ Your reddit API secret    |
|             |
