import requests;
import random;
import schedule;
import time;
import copy;

user_selected = "user_selected"
cs_amzl_innovation_slack_webhook = "https://hooks.slack.com/workflows/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";

class RandomPicker:

    def __init__(self) :
        self.total_users = ["sashtung" , "badpank" , "gmertz" , "rucathi", "shaaga", "anaamar", "agnarula", "dhavalkp", "imgaurav", "kazajaye", "peeyali", "pankha", "rahmknz", "sssomani"];
        self.current_users = [];

    def random_picker(self,users):
        random_user = random.choice(users);
        return random_user

    def make_slack_webcall(self,random_user):

        pload =  {user_selected:random_user}

        print("payload for slack webhook : " , pload);
        r = requests.post(cs_amzl_innovation_slack_webhook, json = pload)
        print(r.text)
        print(r.status_code)
        return r.status_code;

    def main(self):

        print("current users : " , self.current_users);

        #if all users have been picked, recycle
        if len(self.current_users) == 0:
            print("current users is empty");
            self.current_users = copy.deepcopy(self.total_users)

        random_user = self.random_picker(self.current_users)
        print("random user picked " , random_user);
        status_code = self.make_slack_webcall(random_user);

        if status_code != 200 :
            self.make_slack_webcall(random_user);

        else:
            print("removing user : " , random_user);
            self.current_users.remove(random_user);
            print(self.current_users);

if __name__ == "__main__":
    print("starting main ...")
    randomPicker = RandomPicker();
    # schedule.every().day.at("09:00").do(randomPicker.main);
    schedule.every(1).hour.do(randomPicker.main);

    while True:
           schedule.run_pending()
           time.sleep(5)

