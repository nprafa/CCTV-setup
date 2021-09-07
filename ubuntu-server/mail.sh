SUBJECT="TEST TEST TEST"
CONTENTS="This is an email!"
RECEPIENTS="neethaprafa760@gmail.com,jathinsarang@gmail.com"
FROM="neethaprafa760@gmail.com"
/usr/sbin/ssmtp -t << EOF
To: $RECEPIENTS
From: $FROM
Subject: $SUBJECT

$CONTENTS

Cheers,
Me
EOF

