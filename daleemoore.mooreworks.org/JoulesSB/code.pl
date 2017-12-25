# perl code.pl ?

use warnings;
use strict;


use File::Basename;

my @files = @ARGV;
my @suffixlist = (".jpg", ".wav");
my $index = 0;

foreach my $file (@files) {
  my $base= basename $file;
  my ($name,$path,$suffix) = fileparse($file,@suffixlist);
#  print "$name.jpg\n$name.wav\n\n";

  print "<a href=\"#\" onClick=\"return audioPlay('http://DaleEMoore.MooreWorks.Org/~dalem/JoulesSB/$name.wav')\">\n";
  print "<img id=\"jsbutton$index\"\n";
  print "     src=\"http://DaleEMoore.MooreWorks.Org/~dalem/JoulesSB/$name.jpg\"\n";
#  print "     height=\"150\"\n";
  print "     border=\"0\"\n";
  print "     alt=\"jsbutton$index\">\n";
  print "</a>\n\n";
  $index++;
}



# <a href="#"onClick="return audioPlay('http://DaleEMoore.MooreWorks.Org/~dalem/JoulesSB/Baby heartbeat.wav')">
# <img id="jsbutton0" 
#   src="http://DaleEMoore.MooreWorks.Org/~dalem/JoulesSB/Baby heartbeat.jpg" 
#   height="150" 
#   border="0"
#   alt="jsbutton0">
# </a>

#   Change:
# audioPlay parameter.
# jsbutton #.
# src parameter.
