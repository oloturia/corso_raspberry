var i2c = require('i2c-bus');
var sleep = require('sleep');
var GrovePi = require('/home/pi/Dexter/GrovePi/Software/NodeJS/libs').GrovePi;

var board = GrovePi.board;

var DISPLAY_RGB_ADDR = 0x62;
var DISPLAY_TEXT_ADDR = 0x3e;

const setRGB = function (i2c1,rgb) {
	var r = Number('0x'+rgb.substr(1,2));
	var g = Number('0x'+rgb.substr(3,2));
	var b = Number('0x'+rgb.substr(5,2));
	i2c1.writeByteSync(DISPLAY_RGB_ADDR,0,0);
	i2c1.writeByteSync(DISPLAY_RGB_ADDR,1,0);
	i2c1.writeByteSync(DISPLAY_RGB_ADDR,0x08,0xaa);
	i2c1.writeByteSync(DISPLAY_RGB_ADDR,4,r);
	i2c1.writeByteSync(DISPLAY_RGB_ADDR,3,g);
	i2c1.writeByteSync(DISPLAY_RGB_ADDR,2,b);
}

function textCommand(i2c1, cmd) {
	i2c1.writeByteSync(DISPLAY_TEXT_ADDR,0x80,cmd);
}

const setText = function (i2c1, text) {
	textCommand(i2c1, 0x01); //clear display
	sleep.usleep(50000);
	textCommand(i2c1, 0x08 | 0x04); //display on, no cursor
	textCommand(i2c1, 0x28); //2 lines
	sleep.usleep(50000);
	var count = 0;
	var row = 0;
	for (var i = 0, len = text.length; i < len; i++) {
		if(text[i] === '\n' || count === 16) {
			count = 0;
			row ++;
			if (row === 2) break;
			textCommand(i2c1, 0xc0);
			if(text[i] === '\n') continue;
		}
		count ++;
		if (text[i].charCodeAt(0) !== 13) {
			i2c1.writeByteSync(DISPLAY_TEXT_ADDR, 0x40, text[i].charCodeAt(0));
		}
	}
}

module.exports = {
	setRGB,setText
}

