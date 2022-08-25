# MMM-Reddit-News-Ticker

This is a module for the [MagicMirror²](https://github.com/MichMich/MagicMirror/).

![screenshot](images\screenshot1.png)

## Using the module

Requires [python3](https://www.python.org/downloads/).

You will need to get your own [client ID and secret](https://www.reddit.com/prefs/apps) from reddit.

![reddit api](images\reddit-api.png)

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
