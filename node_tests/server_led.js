var GrovePi = require('/home/pi/Dexter/GrovePi/Software/NodeJS/libs').GrovePi; //library for GrovePi HAT
var http = require('http'); //http server
var fs = require('fs'); //filesystem
var lcd = require('./lcd_display'); //lcd_display
var i2c = require('i2c-bus'); //i2c 
var qs = require('querystring'); //data parsing

var led = new GrovePi.sensors.DigitalOutput(4);
var DHTDigitalSensor = GrovePi.sensors.DHTDigital;
var dhtSensor = new DHTDigitalSensor(7, DHTDigitalSensor.VERSION.DHT11, DHTDigitalSensor.CELSIUS);
var dht_value
dhtSensor.on('change', function(dht_res) {
						dht_value = dht_res
						})
dhtSensor.watch(500);

var board;

var DISPLAY_RGB_ADDR = 0x62;
var DISPLAY_TEXT_ADDR = 0x3e;

function start() {

	
	board = new GrovePi.board({
		debug: true,
		onError: function(err) {
			console.log(err)
		},
		onInit: function(res) {
			http.createServer(function(req,res) {
				if (req.url == '/style.css') {
					fs.readFile('./style.css', function(err,data) {
						res.writeHead(200, {'Content-Type': 'text/css'});
						res.write(data);
						return res.end()
					});
				} else if (req.url == '/dht11') {
					res.writeHead(200, {'Content-Type': 'text/plain'});	
					res.write(dht_value[0].toString());
					return res.end()
				} else {
					if(req.method === 'POST') {
						var data = '';
						req.on('data', function(chunk) {
								data += chunk;
						});
						req.on('end', function() {
							var post = qs.parse(data);
							console.log(post)
							if (post['led'] === 'on') {
								led.turnOn();
							} else if (post['led'] === 'off') {
								led.turnOff();
							}
							if (post['lcd_text'] != undefined) {
									var i2c1 = i2c.openSync(1);
									lcd.setText(i2c1,post['lcd_text']);
									lcd.setRGB(i2c1,post['lcd_color']);
									i2c1.closeSync();
							}
						});
					} 
					fs.readFile('./led.html', function(err,data) {
						res.writeHead(200, {'Content-Type': 'text/html'});
						res.write(data);
						return res.end();
					});
				}
			}).listen(8080);
		}
	})
	board.init();
}


function onExit(err){
	console.log('exiting...')
	board.close()
	process.removeAllListeners()
	process.exit()
	if (typeof err != 'undefined')
		console.log(err)
}
start()
process.on('SIGINT',onExit)
