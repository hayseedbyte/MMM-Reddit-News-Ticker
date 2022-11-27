var NodeHelper = require('node_helper');
const cp = require('child_process');
const path = require('path');

module.exports = NodeHelper.create({
  socketNotificationReceived: function (notification, payload) {
    if (notification === 'PULL_NEWS') {
      console.log(process.env.PATH);
      const execOptions = {
        cwd: '~/MagicMirror/modules/MMM-Reddit-News-Ticker/',
        env: null,
        encoding: 'utf8',
        timeout: 0,
        PATH: process.env.PATH,
      };
      // console.log(cwd);
      console.log(process.env.PATH);
      console.log('!!!!!!!!!!!');
      const id = payload[0];
      const secret = payload[1];
      const out = cp.exec(
        `/usr/bin/python3 reddit-news-str.py ${id} ${secret}`,
        execOptions,
        (err, stdout, stderr) => {
          this.sendSocketNotification('TITLES', stdout);
          console.log(err);
          console.log(stderr);
        }
      );
    }
    if (notification === 'DOM_OBJECTS_CREATED') {
      const data = payload;
      const string = data.toString();
      const length = string.length;
      const time = Math.round(length / 12);
      this.sendSocketNotification('TIME', time);
      this.joinData(data);
    }
  },

  joinData: function (arr) {
    const ray = arr.split('~');
    const joined = ray.join('&nbsp&nbsp&nbsp&nbsp::&nbsp&nbsp&nbsp&nbsp');
    this.sendSocketNotification('ARR', joined);
  },
});
