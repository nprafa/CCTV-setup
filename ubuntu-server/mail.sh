SUBJECT="TEST TEST TEST"
CONTENTS="This is an email!"

/usr/sbin/ssmtp -t << EOF
To: neethaprafa760@gmail.com
From: neethaprafa760@gmail.com
Subject: $SUBJECT

$CONTENTS

Cheers,
Me
EOF
