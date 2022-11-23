Module.register('MMM-Reddit-News-Ticker', {
  defaults: {
    updateInterval: 60000, // 2.5 hours
    retryDelay: 5000,
  },

  requiresVersion: '2.1.0', // Required version of MagicMirror

  start: function () {
    var home = this;
    console.log(home.name + 'START');
    const id = home.config.client_id;
    const secret = home.config.secret;
    const api = [id, secret];
    home.getData(api);
    setInterval(function () {
      self.updateDom();
    }, home.config.updateInterval);
  },

  getData: function (data) {
    const retry = true;
    // const data = this.data;
    this.sendSocketNotification('PULL_NEWS', data);
  },
  getDom: function () {
    const moduleDiv = document.createElement('div');
    if (document.querySelector('.hwrap') === null) {
      const hwrap = document.createElement('div');
      const hmove = document.createElement('div');
      const hitem = document.createElement('div');
      moduleDiv.appendChild(hwrap);
      hwrap.appendChild(hmove);
      hmove.appendChild(hitem);
      hwrap.classList.add('hwrap');
      hmove.classList.add('hmove');
      hitem.classList.add('hitem');
    }
    return moduleDiv;
  },

  getScripts: function () {
    return [];
  },

  getStyles: function () {
    return ['MMM-Reddit-News-Ticker.css'];
  },

  // Load translations files
  getTranslations: function () {
    return {
      en: 'translations/en.json',
      es: 'translations/es.json',
    };
  },

  processData: function (data) {
    this.loaded = true;
    this.sendSocketNotification('DOM_OBJECTS_CREATED', data);
  },
  injectHTML: function (str) {
    const hitem = document.querySelector('.hitem');
    hitem.innerHTML = str;
  },

  socketNotificationReceived: function (notification, payload) {
    const self = this;
    switch (notification) {
      case 'TIME':
        console.log(this.name + ' ⌛');
        const time = payload;
        const hitem = document.querySelector('.hitem');
        hitem.style.animationName = 'tickerh';
        hitem.style.animationDuration = `${time}s`;
        hitem.style.animationTimingFunction = 'linear';
        hitem.style.animationIterationCount = 'infinite';
        break;
      case 'ARR':
        console.log(this.name + ' 🏴‍☠️');
        this.injectHTML(payload);
        break;
      case 'TITLES':
        console.log(this.name + ' 📰');
        this.processData(payload);
        break;
    }
  },
});
