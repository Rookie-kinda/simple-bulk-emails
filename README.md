# simple-bulk-emails
This Code Helps you send Bulk simple emails, I am still struggling to make it attach pictures, but it works as the base model was intended, feel free to add some modifications and pull reqs, and we can talk it over, i'll add some modifications for it over time

You need to turn on 2-step verfication, after activating it remove everything in the link from /signinoptions till the end and put instead /apppasswords, after entering your email password, under "select app" select *other(custom name)*, then choose a name, click on generate, then copy the 16 character password it will show you, paste it in the "password" argument, that's all you need to do

Other than that, you just fill in the proper arguments, and enjoy :D


***IMPORTANT DISCLAIMER***
Gmail has a 500 Email/day limit + it can detect spam mails and block your account if you were indeed spotted, so make sure if you're sending bulks, after reading the emails into the code using pandas for instance, make sure you don't exceed 500 emails, and that you add a sleep() function for maybe a min and a half or two minutes ig
