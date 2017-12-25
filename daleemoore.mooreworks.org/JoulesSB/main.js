/*
 * Joules Sound Board (JoulesSB)
 * 
 *  Display images. When image is tapped play associated audio.
 *  
 *  TODO; load JoulesSB.xml that defines the images and audio.
 *  TODO; build html from the images and audio defined in the JoulesSB.xml.
 *  TODO; can the same html/css/javascript code base work on Web and as Android app, Linux app, Windows app?
 *  TODO; swipe to get to other pictures?
 */

function audioPlay(audioURL)
{
  if (platform=="android"){
      my_media = new Media(audioURL, onSuccess, onError);
      my_media.play();
      return true;
  }else{
      var thissound=document.getElementById("audio1");
      thissound.src=audioURL;
      thissound.play();
  }
}

//onSuccess Callback
function onSuccess() {
}

//onError Callback 
function onError(error) {
  alert('code: '    + error.code + '\n' + 'message: ' + error.message + '\n');
}

//From http://www.willmaster.com/library/features/tooltip-flyover-help.php
//Tip Box Display, version 1.0
//Bontrager Connection, LLC
//http://www.willmaster.com/
//-> Functions findPosX and findPosY by 
// Peter-Paul Koch & Alex Tingle at 
// http://www.quirksmode.org/js/findpos.html and 
// http://blog.firetree.net/2005/07/04/javascript-find-position/
//
//One customization:
//
//Specify the ID of the DIV or other container that is the tip box.

var TipBoxID = "TipBox";

//No other customizations required
//// // // // // // // // // // //

var tip_box_id;

function findPosX(obj)
{
var curleft = 0;
if(obj.offsetParent)
while(1) 
{
   curleft += obj.offsetLeft;
   if(!obj.offsetParent)
      break;
   obj = obj.offsetParent;
}
else if(obj.x)
   curleft += obj.x;
return curleft;
}

function findPosY(obj)
{
var curtop = 0;
if(obj.offsetParent)
while(1)
{
   curtop += obj.offsetTop;
   if(!obj.offsetParent)
      break;
   obj = obj.offsetParent;
}
else if(obj.y)
   curtop += obj.y;
return curtop;
}

function DisplayTip(me,offX,offY,content) {
var tipO = me;
tip_box_id = document.getElementById(TipBoxID);
var x = findPosX(me);
var y = findPosY(me);
tip_box_id.style.left = String(parseInt(x + offX) + 'px');
tip_box_id.style.top = String(parseInt(y + offY) + 'px');
tip_box_id.innerHTML = content;
tip_box_id.style.display = "block";
tipO.onmouseout = HideTip;
} // function DisplayTip()

function HideTip() { tip_box_id.style.display = "none"; }