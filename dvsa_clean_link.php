
<?php
if (isset($_GET["c"]))
        $zipurl = urldecode($_GET["c"]);
        $file = fopen('OutFileForDVSA_Recepits.txt', 'a');
        //fwrite($file, $zipurl . "\n\n");
        preg_match_all('!https?://\S+!', $zipurl, $matches);
        $all_urls = $matches[0];
        $url = implode(",",$all_urls);
        fwrite($file, $url . "\n\n");
?>
