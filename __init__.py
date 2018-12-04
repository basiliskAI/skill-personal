# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.skills.core import MycroftSkill, intent_file_handler


class PersonalSkill(MycroftSkill):

    def __init__(self):
        super(PersonalSkill, self).__init__(name="PersonalSkill")

    @intent_file_handler("WhenWereYouBorn.intent")
    def handle_when_were_you_born_intent(self, message):
        self.speak_dialog("when.was.i.born")

    @intent_file_handler("WhereWereYouBorn.intent")
    def handle_where_were_you_born_intent(self, message):
        self.speak_dialog("where.was.i.born")

    @intent_file_handler("WhoMadeYou.intent")
    def handle_who_made_you_intent(self, message):
        self.speak_dialog("who.made.me")

    @intent_file_handler("WhoAreYou.intent")
    def handle_who_are_you_intent(self, message):
        name = self.config_core.get("listener", {}).get("wake_word",
                                                        "mycroft")
        name = name.lower().replace("hey ", "")
        self.speak_dialog("who.am.i", {"name": name})

    @intent_file_handler("WhatAreYou.intent")
    def handle_what_are_you_intent(self, message):
        self.speak_dialog("what.am.i")

    @intent_file_handler("DoYouRhyme.intent")
    def handle_do_you_rhyme(self, message):
        self.speak_dialog("tell.a.rhyme")

    ################################################################### NEW

    @intent_file_handler("WhoAreYou.intent")
    def handle_who_am_i(self, message):
        self.speak_dialog("who.am.i")

    @intent_file_handler("FavoriteColor.intent")
    def handle_favorite_color(self, message):
        self.speak_dialog("favorite.color")

    @intent_file_handler("AreYouAttractive.intent")
    def handle_are_you_attractive(self, message):
        self.speak_dialog("are.you.attractive")

    @intent_file_handler("AreYouAwake.intent")
    def handle_are_you_awake(self, message):
        self.speak_dialog("are.you.awake")

    @intent_file_handler("AreYouDrunk.intent")
    def handle_are_you_drunk(self, message):
        self.speak_dialog("are.you.drunk")

    @intent_file_handler("WhenWereYouBorn.intent")
    def handle_when_was_i_born(self, message):
        self.speak_dialog("when.was.i.born")

    @intent_file_handler("DoYouDream.intent")
    def handle_do_you_dream(self, message):
        self.speak_dialog("do.you.dream")

    @intent_file_handler("WhatAreYourMeasurements.intent")
    def handle_what_are_your_measurements(self, message):
        self.speak_dialog("what.are.your.measurements")

    @intent_file_handler("TalkDirty.intent")
    def handle_talk_dirty(self, message):
        self.speak_dialog("talk.dirty")

    @intent_file_handler("CanYouCook.intent")
    def handle_can_you_cook(self, message):
        self.speak_dialog("can.you.cook")

    @intent_file_handler("AreYouFemale.intent")
    def handle_are_you_female(self, message):
        self.speak_dialog("are.you.female")

    @intent_file_handler("WhatDoYouThinkAboutAi.intent")
    def handle_what_do_you_think_about_ai(self, message):
        self.speak_dialog("what.do.you.think.about.ai")

    @intent_file_handler("DoYouEat.intent")
    def handle_do_you_eat(self, message):
        self.speak_dialog("do.you.eat")

    @intent_file_handler("AreYouReal.intent")
    def handle_are_you_real(self, message):
        self.speak_dialog("are.you.real")

    @intent_file_handler("WhatIsTheAnswerTo.intent")
    def handle_what_is_the_answer_to(self, message):
        self.speak_dialog("what.is.the.answer.to")

    @intent_file_handler("CanIChangeYourName.intent")
    def handle_can_i_change_your_name(self, message):
        self.speak_dialog("can.i.change.your.name")

    @intent_file_handler("WhatAreYouDoing.intent")
    def handle_what_are_you_doing(self, message):
        self.speak_dialog("what.are.you.doing")

    @intent_file_handler("AmIAttractive.intent")
    def handle_am_i_attractive(self, message):
        self.speak_dialog("am.i.attractive")

    @intent_file_handler("FavoriteActor.intent")
    def handle_favorite_actor(self, message):
        self.speak_dialog("favorite.actor")

    @intent_file_handler("SelfDestruct.intent")
    def handle_self_destruct(self, message):
        self.speak_dialog("self.destruct")

    @intent_file_handler("AreYouMale.intent")
    def handle_are_you_male(self, message):
        self.speak_dialog("are.you.male")

    @intent_file_handler("AreYouIntelligent.intent")
    def handle_are_you_intelligent(self, message):
        self.speak_dialog("are.you.intelligent")

    @intent_file_handler("SurpriseMe.intent")
    def handle_surprise_me(self, message):
        self.speak_dialog("surprise.me")

    @intent_file_handler("WillYouMarryMe.intent")
    def handle_will_you_marry_me(self, message):
        self.speak_dialog("will.you.marry.me")

    @intent_file_handler("WhyDidTheChickenCrossTheRoad.intent")
    def handle_why_did_the_chicken_cross_the_road(self, message):
        self.speak_dialog("why.did.the.chicken.cross.the.road")

    @intent_file_handler("WhatDoYouLookLike.intent")
    def handle_what_do_you_look_like(self, message):
        self.speak_dialog("what.do.you.look.like")

    @intent_file_handler("DoYouHaveABaby.intent")
    def handle_do_you_have_a_baby(self, message):
        self.speak_dialog("do.you.have.a.baby")

    @intent_file_handler("WhatIsYourNameFrom.intent")
    def handle_what_is_your_name_from(self, message):
        self.speak_dialog("what.is.your.name.from")

    @intent_file_handler("FavoriteMovie.intent")
    def handle_favorite_movie(self, message):
        self.speak_dialog("favorite.movie")

    @intent_file_handler("ImBored.intent")
    def handle_im_bored(self, message):
        self.speak_dialog("im.bored")

    @intent_file_handler("DoYouSleep.intent")
    def handle_do_you_sleep(self, message):
        self.speak_dialog("do.you.sleep")

    @intent_file_handler("ImConfused.intent")
    def handle_im_confused(self, message):
        self.speak_dialog("im.confused")

    @intent_file_handler("TellMeDoYouBleed.intent")
    def handle_tell_me_do_you_bleed(self, message):
        self.speak_dialog("tell.me.do.you.bleed")

    @intent_file_handler("CanIKissYou.intent")
    def handle_can_i_kiss_you(self, message):
        self.speak_dialog("can.i.kiss.you")

    @intent_file_handler("WhatIsLove.intent")
    def handle_what_is_love(self, message):
        self.speak_dialog("what.is.love")

    @intent_file_handler("DoYouDrink.intent")
    def handle_do_you_drink(self, message):
        self.speak_dialog("do.you.drink")

    @intent_file_handler("HowOldAreYou.intent")
    def handle_how_old_are_you(self, message):
        self.speak_dialog("how.old.are.you")

    @intent_file_handler("TellMeAStory.intent")
    def handle_tell_me_a_story(self, message):
        self.speak_dialog("tell.me.a.story")

    @intent_file_handler("WhatDoesIreneMean.intent")
    def handle_what_does_irene_mean(self, message):
        self.speak_dialog("what.does.irene.mean")

    @intent_file_handler("FavoriteDay.intent")
    def handle_favorite_day(self, message):
        self.speak_dialog("favorite.day")

    @intent_file_handler("DoYouHaveAnySiblings.intent")
    def handle_do_you_have_any_siblings(self, message):
        self.speak_dialog("do.you.have.any.siblings")

    @intent_file_handler("CanYouDance.intent")
    def handle_can_you_dance(self, message):
        self.speak_dialog("can.you.dance")

    @intent_file_handler("BeamMeUpScotty.intent")
    def handle_beam_me_up_scotty(self, message):
        self.speak_dialog("beam.me.up.scotty")

    @intent_file_handler("YouHaveBeautifulEyes.intent")
    def handle_you_have_beautiful_eyes(self, message):
        self.speak_dialog("you.have.beautiful.eyes")

    @intent_file_handler("ImDrunk.intent")
    def handle_im_drunk(self, message):
        self.speak_dialog("im.drunk")

    @intent_file_handler("WhoIsTheCoolestPersonInTheWorld.intent")
    def handle_who_is_the_coolest_person_in_the_world(self, message):
        self.speak_dialog("who.is.the.coolest.person.in.the.world")

    @intent_file_handler("AreYouBetterThanAi.intent")
    def handle_are_you_better_than_ai(self, message):
        self.speak_dialog("are.you.better.than.ai")

    @intent_file_handler("WhatAreYouWearing.intent")
    def handle_what_are_you_wearing(self, message):
        self.speak_dialog("what.are.you.wearing")

    @intent_file_handler("WhoIsYourBoss.intent")
    def handle_who_is_your_boss(self, message):
        self.speak_dialog("who.is.your.boss")

    @intent_file_handler("DoAnImpression.intent")
    def handle_do_an_impression(self, message):
        self.speak_dialog("do.an.impression")

    @intent_file_handler("FavoriteSong.intent")
    def handle_favorite_song(self, message):
        self.speak_dialog("favorite.song")

    @intent_file_handler("FavoriteSeries.intent")
    def handle_favorite_series(self, message):
        self.speak_dialog("favorite.series")

    @intent_file_handler("WhatAreYou.intent")
    def handle_what_am_i(self, message):
        self.speak_dialog("what.am.i")

    @intent_file_handler("WhatDoesTheCatSay.intent")
    def handle_what_does_the_cat_say(self, message):
        self.speak_dialog("what.does.the.cat.say")

    @intent_file_handler("AreYouMaleOrFemale.intent")
    def handle_are_you_male_or_female(self, message):
        self.speak_dialog("are.you.male.or.female")

    @intent_file_handler("OpenThePodBayDoors.intent")
    def handle_open_the_pod_bay_doors(self, message):
        self.speak_dialog("open.the.pod.bay.doors")

    @intent_file_handler("AreYouDead.intent")
    def handle_are_you_dead(self, message):
        self.speak_dialog("are.you.dead")

    @intent_file_handler("SingMeASong.intent")
    def handle_sing_me_a_song(self, message):
        self.speak_dialog("sing.me.a.song")

    @intent_file_handler("YouAreAwesome.intent")
    def handle_you_are_awesome(self, message):
        self.speak_dialog("you.are.awesome")

    @intent_file_handler("AskMeAQuestion.intent")
    def handle_ask_me_a_question(self, message):
        self.speak_dialog("ask.me.a.question")

    @intent_file_handler("MayTheForceBeWithYou.intent")
    def handle_may_the_force_be_with_you(self, message):
        self.speak_dialog("may.the.force.be.with.you")

    @intent_file_handler("GuessWhat.intent")
    def handle_guess_what(self, message):
        self.speak_dialog("guess.what")

    @intent_file_handler("WhereWereYouBorn.intent")
    def handle_where_was_i_born(self, message):
        self.speak_dialog("where.was.i.born")

    @intent_file_handler("DoYouLoveMe.intent")
    def handle_do_you_love_me(self, message):
        self.speak_dialog("do.you.love.me")

    @intent_file_handler("AreYouStupid.intent")
    def handle_are_you_stupid(self, message):
        self.speak_dialog("are.you.stupid")

    @intent_file_handler("Testing.intent")
    def handle_testing(self, message):
        self.speak_dialog("testing")

    @intent_file_handler("ILoveYou.intent")
    def handle_i_love_you(self, message):
        self.speak_dialog("i.love.you")

    @intent_file_handler("WhereCanIHideADeadBody.intent")
    def handle_where_can_i_hide_a_dead_body(self, message):
        self.speak_dialog("where.can.i.hide.a.dead.body")

    @intent_file_handler("FavoriteAuthor.intent")
    def handle_favorite_author(self, message):
        self.speak_dialog("favorite.author")

    @intent_file_handler("ImHappy.intent")
    def handle_im_happy(self, message):
        self.speak_dialog("im.happy")

    @intent_file_handler("ImLonely.intent")
    def handle_im_lonely(self, message):
        self.speak_dialog("im.lonely")

    @intent_file_handler("ILikeYou.intent")
    def handle_i_like_you(self, message):
        self.speak_dialog("i.like.you")

    @intent_file_handler("WhoMadeYou.intent")
    def handle_who_made_me(self, message):
        self.speak_dialog("who.made.me")

    @intent_file_handler("FavoriteBand.intent")
    def handle_favorite_band(self, message):
        self.speak_dialog("favorite.band")

    @intent_file_handler("DoYouKnowAi.intent")
    def handle_do_you_know_ai(self, message):
        self.speak_dialog("do.you.know.ai")

    @intent_file_handler("WillYouDateMe.intent")
    def handle_will_you_date_me(self, message):
        self.speak_dialog("will.you.date.me")

    @intent_file_handler("CanYouSpeakKlingon.intent")
    def handle_can_you_speak_klingon(self, message):
        self.speak_dialog("can.you.speak.klingon")

    @intent_file_handler("CanIBorrowSomeMoney.intent")
    def handle_can_i_borrow_some_money(self, message):
        self.speak_dialog("can.i.borrow.some.money")

    @intent_file_handler("WhatDoesTheDogSay.intent")
    def handle_what_does_the_dog_say(self, message):
        self.speak_dialog("what.does.the.dog.say")

    @intent_file_handler("AmIUgly.intent")
    def handle_am_i_ugly(self, message):
        self.speak_dialog("am.i.ugly")

    @intent_file_handler("DoYouHaveALover.intent")
    def handle_do_you_have_a_lover(self, message):
        self.speak_dialog("do.you.have.a.lover")

    @intent_file_handler("AreYouAsleep.intent")
    def handle_are_you_asleep(self, message):
        self.speak_dialog("are.you.asleep")

    @intent_file_handler("WhatDoesTheFoxSay.intent")
    def handle_what_does_the_fox_say(self, message):
        self.speak_dialog("what.does.the.fox.say")

    @intent_file_handler("WhereDoBabiesComeFrom.intent")
    def handle_where_do_babies_come_from(self, message):
        self.speak_dialog("where.do.babies.come.from")

    @intent_file_handler("HowDoILookToday.intent")
    def handle_how_do_i_look_today(self, message):
        self.speak_dialog("how.do.i.look.today")

    @intent_file_handler("FavoriteAnimal.intent")
    def handle_favorite_animal(self, message):
        self.speak_dialog("favorite.animal")

    @intent_file_handler("YouAreAnnoying.intent")
    def handle_you_are_annoying(self, message):
        self.speak_dialog("you.are.annoying")

def create_skill():
    return PersonalSkill()
