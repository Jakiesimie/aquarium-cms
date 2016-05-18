<?php
// ----------------------------------------------------------------------
// THIS FILE IS GENERATED BY BACKEND-API. PLEASE! DO NOT MODIFY ANYTHING!
// ----------------------------------------------------------------------
$data = <<< EOT
[{"id":1,"tank":2,"name_eng":"Tricolor sharkminnow","name_arabic":"الإسم الشائع: قرش المِنْوَة ثلاثى الألوان","scientific_name":"Balantiocheilos melanopterus","image":"http://testserver/media/aquarium/Tricolor-sharkminnow.png","distribution_label_eng":"Mekong and Chao Phraya River basins, Borneo, Malay Peninsula and  Sumatra, Asia","distribution_label_arabic":"التوزيع الجغرافى: حوض أنهار الميكونج ,تشاو , فرايا,بورنيو,شبه جزيرة الملايو, سومطره وآسيا.","distribution_image":null,"description_eng":"The Shark minnow name comes from their torpedo shaped body and large fins.  These fish however, are not in fact true sharks.","description_arabic":"يطلق عليها أسم القرش مجازاً بسب جسمه الذى يشبه شكل الطوربيد ولكنه ليس من أسماك القرش فى الواقع."},{"id":2,"tank":2,"name_eng":"Assorted Rainbowfish","name_arabic":"أسماك قوس قزح المتنوعة","scientific_name":"Melanotaenia","image":"http://testserver/media/aquarium/Assorted-Rainbowfish.png","distribution_label_eng":"New Guinea","distribution_label_arabic":"التوزيع الجغرافى: غينيا الجديدة","distribution_image":null,"description_eng":"As their name suggests, these fish get their common name from their colourful scales.","description_arabic":"كما يوحى اسمها, حصلت هذه الأسماك على اسمها الشائع عن طريق قشورها الغنية بالألوان."},{"id":3,"tank":2,"name_eng":"Molly","name_arabic":"الإسم الشائع: سمكة مولى","scientific_name":"Poecilia spp","image":"http://testserver/media/aquarium/Molly.png","distribution_label_eng":"Central America","distribution_label_arabic":"التوزيع الجغرافى: أمريكا الوسطى","distribution_image":null,"description_eng":"These fish have the ability  to live in  both  fresh and saltwater.","description_arabic":"تُعبر عن عن سعادتها بالتأرجح ذهاباًوعودة فى نفس المكان. هذا السلوك يُعرف بالإهتزاز."}]
EOT;


function parse($text) {
    // Damn pesky carriage returns...
    $text = str_replace("\r\n", "\n", $text);
    $text = str_replace("\r", "\n", $text);

    // JSON requires new line characters be escaped
    $text = str_replace("\n", "\\n", $text);
    return $text;
}



header('Content-Type: application/json');
echo parse($data);
exit;
