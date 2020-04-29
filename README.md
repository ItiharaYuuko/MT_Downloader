# MT_Downloader
Multithreading downloader for free movies, using the m3u8 type.

# Help for using
At first you have to get the movies url, use the browser debuger
press F12 to open the control panel, after select the network button
and the media button reload the page, watching the right window, paste 
the url into the srcipt, and delete the context after last '\\',
paste the url into the scripts 'usage_information'dictionary which
in the __main__ function.
Second, get the url after last '\\' context, this is your target 
filename, and analysis the structure of the name.It may combinate
with strings and integers, please split it with your self. If you
changed the website to download you should reanalysis the url.
Third, drag the slider to the end of the player, looking for the
debugers left panel, watching the get requests echo, when the file
do not loading, the serial number of the file should paste into the
'usage_information' dictionary to update the 'files_count' field.
In the end, when you want to change the numbers of thread, you only
should chinge the variable 'st' which in the __main__ function.
                                                      
  Enjoy
  @ItiharaYuuko
