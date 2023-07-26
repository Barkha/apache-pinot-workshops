# Getting Started with Apache Pinot™: Anomaly Detection with ThirdEye

## Introduction

This is an intro level workshop and is designed to get you started with ThirdEye Anomaly Detection Platform on an existing Pinot Cluster. In order to complete this workshop, you should have a StarTree Cloud account.

## Learning Objectives

In this workshop you will learn how to:

- Access and navigate the ThirdEye portal
- Setup Data Source & Ingest Data
- Create and Alert
- Examine Anomalies
- Create Events

## Prerequisits

In order to be effective in this workshop, you should:

- Have some Apache Pinot experience OR have finished [previous workshop](../GettingStartedBatch/README.md)
- Have a Startree Cloud Account [sign up here](https://startree.ai/saas-signup)

## Challenges

In this workshop, we will be completing four challenges.  Each challenge is designe to get you familiar with the platform and introduce you to the basic functionality of the ThirdEye Platform.

### 1 - Access ThirdEye Portal

Log into the Startree Cloud Portal by navigating to <https://startree.cloud>

**NOTE** that if you are doing this workshop with a StarTree host, they will share the URL to logon with you.  If you are signed up for StarTree Cloud, use that URL, and make sure you have ThirdEye enabled.

You should see the follows:

![StarTree Cloud Screen](/images/thirdeye/thirdeye1.png "StarTree Cloud")

**NOTE** that if you don't see ThirdEye link Active, you may need to contact StarTree support enable it.

Click on the ThirdEye 

You should see something like this:

![ThirdEye Screen](/images/thirdeye/thirdeye2.png "ThirdEye Start Page")

### 2 - Connect to Dataset

Now that we have access to the ThridEye portal.  We will start with setting up our Data for ThirdEye.

Click on the "Configuration" on the left hand side menu.

![ThirdEye Screen](/images/thirdeye/thirdeye3.png "ThirdEye Data Configuration Page")

Select the Create button, Onboard Dataset option.

For this challenge, we will select the exsisting Apache Pinot source, called "pinot".

Next, we will select the datasets available to us.  For this challenge, let's select websiteAnomalies. 

**Note** if you are using a shared environment, use one of the websiteAnomalies(x)

![ThirdEye Screen](/images/thirdeye/thirdeye4.png "ThirdEye Data Configuration Page")

Now, select Submit.

That's it!  You have now configures the Datasource for Anomaly detection with ThirdEye.

### 3 - Create Alert

Next, we will create an alert.  Let's start by selecting the  "Alert" from the left hand side menu.

![ThirdEye Screen](/images/thirdeye/thirdeye5.png "ThirdEye Alert Configuration Page")

This will take you to a page where you can select what type of alert you can create.

Here's what is available to choose from:

1. Basic Alert
2. Multi-dimensional alert

Dimension Exploration gives users the ability to create alerts for every value of a certain dimension or combination of dimensions.

Here's the visual:

![ThirdEye Screen](/images/thirdeye/thirdeye6.png "ThirdEye Alert Configuration Page")

For our porposes, we will choose Multi-dimensional alert.  This should bring up the next step - the CoHort recommender.

![ThirdEye Screen](/images/thirdeye/thirdeye7.png "ThirdEye Alert Configuration Page")

At this point, you should be able to create an alert using the dataset you onboarded.

Here's what we will be using for each of the values:

1. Dataset: The dataset you onboarded
2. Metric:  Let's use click
3. Aggregation Dunction:  Let's use COUNT
4. Dimentions: Let's use country, browser and platform
5. Date range: Let's narrow it down to 2021
6. Query filter: Ignore for now
7. Contribution percentage: let's leave it at 5%.

![ThirdEye Screen](/images/thirdeye/thirdeye8.png "ThirdEye Alert Configuration Page")

Now select Generate Dimentions to Monitor to see what your dimensions look like.

You should see something like this:

![ThirdEye Screen](/images/thirdeye/thirdeye9.png "ThirdEye Alert Configuration Page")

Let's select all the dimensions, and click on the button Create Multi-dimension alert.

![ThirdEye Screen](/images/thirdeye/thirdeye10.png "ThirdEye Alert Configuration Page")

You should now be one step further in the workflow, where you can select the granularity. The default is Daily, but you can change it.  Load chart to see what the pattern looks like.  You can also change the date range to see what shows up.

Choose AVG as the Aggregation function, and hourly as te granularity, reload preview and scroll down to country are.  Notice some spikes.

![ThirdEye Screen](/images/thirdeye/thirdeye11.png "ThirdEye Alert Configuration Page")

For our alert, I am going to choose avg daily.
Select Next to move to the algorithm selection.

For this scenario, I am not looking for seasonal variation in the click rates, and am focused on the day to day click rates.  So, I am going to select the Mean Varience Rule.

![ThirdEye Screen](/images/thirdeye/thirdeye12.png "ThirdEye Alert Configuration Page")

Select the Next button, which takes you to the Tune alert page.
Here, you can adjust the sensivity, seasonality, and lookback period. You can load chart to see the alerts that show up based on your tuning.

For our scenario, we will pick the defaults.

![ThirdEye Screen](/images/thirdeye/thirdeye13.png "ThirdEye Alert Configuration Page")

Select Next to move to the anomaly filter page.  Here, you can select the Filters and sensitivity button to adjust your anomaly detection.  Examples are adding exception such as don't monitor on weekends etc.

![ThirdEye Screen](/images/thirdeye/thirdeye14.png "ThirdEye Alert Configuration Page")

For this scenario, I am not going to setup any filter.
Select Next, provide a meaningful name, and save.

Voila!  You have created your first alert!

### 4 - Examine Anomalies

Now that we have created an alert, let's dive into how to look at your anomalies.

From the Alert menu, select the alert you just created.

You should see somthing like this:

![ThirdEye Screen](/images/thirdeye/thirdeye15.png "ThirdEye Examine Anomalies Page")

You can click on the View Details link to see the anomalies for a particular set of dimentions:

![ThirdEye Screen](/images/thirdeye/thirdeye16.png "ThirdEye Examine Anomalies Page")

You can click on individual anomalies, or select a section to view it in detail.

Let's click on an anomaly.

![ThirdEye Screen](/images/thirdeye/thirdeye17.png "ThirdEye Examine Anomalies Page")

Select the Investigate Anomaly button to do some root cause analysis.

![ThirdEye Screen](/images/thirdeye/thirdeye18.png "ThirdEye Examine Anomalies Page")

Here, you can look at the heatmap, the Top contributors and events.  We will talk events in the next exercise.  

The heat maps shows you what the contributing fators were related to the anomaly.  Blue indicates higher than normal numbers, red indicated lower than normal numbers, and grey is baseline.

Top contributor show you what caused the anomaly.

You also have the option to tag this as "real" or flase positive.

Select the drop down from the "Is this an anomaly" and choose an option that fits your scenario.

You can save the investigation, revisit later or share it with someone in you team.

### 5 - Create Events

Let's now create an event.

Navigate to the configuration menu, and select the Events tab.

![ThirdEye Screen](/images/thirdeye/thirdeye19.png "ThirdEye Events Page")

Select Create, Create Event.

Enter a name, type (string), start and end dates.

Optionally, you can add some metadata tags.  These can be used for catagorization purposes.  Click create event to save.

![ThirdEye Screen](/images/thirdeye/thirdeye20.png "ThirdEye Events Page")

To use a created event, in the Anomalies page, choose the events tab and associate the event to the anomaly.

![ThirdEye Screen](/images/thirdeye/thirdeye21.png "ThirdEye Events Page")

### 6 - Create Subscription Groups

Let's now create Subscription groups and associate some alert with them.

From the Configuration Menu, select Subscription Groups.  Select Create Subscription Group.

Enter the Name and Schedule.  You can either use Cron syntax or use the UI to setup the schedule.

You can also add Emails, slack channel or use a webhook to connect to the Subscription Group.

![ThirdEye Screen](/images/thirdeye/thirdeye22.png "ThirdEye Subscription Groups Page")

Select the Next button to setup what alerts you want to be notifeid on.  Save to save your Subscription Group.

When you create new alerts, you can use the existing Subscription Groups to add the alert notification to.

![ThirdEye Screen](/images/thirdeye/thirdeye23.png "ThirdEye Subscription Groups Page")

Voila!  You should now recieve alerts when anomalies happen!

### 7 - Tear Down

From the Alerts Menu, select and delete any alerts you have created.
Fom the configuration Menu, select and delete:

1. Subscription Groups
2. Events
3. Datasets