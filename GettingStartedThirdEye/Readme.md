# Getting Started with Apache Pinot™: Anomaly Detection with ThirdEye

## Introduction

This intro level workshop will help you get started with ThirdEye Anomaly Detection Platform on an existing Pinot Cluster. To complete this workshop, you should have a [StarTree Cloud account](https://startree.ai/saas-signup).

## Learning objectives

In this workshop, you will learn how to:

- Access and navigate the ThirdEye portal
- Set up a data source and ingest data
- Create and alert
- Examine anomalies
- Create events

## Prerequisites

To be effective in this workshop, you should:

- Have some Apache Pinot experience *or* have finished the [previous workshop](../GettingStartedBatch/README.md)
- Have a Startree Cloud account [sign up here](https://startree.ai/saas-signup)

## Challenges

In this workshop, we'll complete four challenges. Each challenge is designed to get you familiar with the platform and introduce you to the basic functionality of the ThirdEye platform.

### 1 - Access ThirdEye Portal

Log into the Startree Cloud Portal by navigating to <https://startree.cloud>.

**Note:** If you are doing this workshop with a StarTree host, they will share the URL to log on with you. If you are signed up for StarTree Cloud, use that URL, and make sure you have ThirdEye enabled.

You should see the following:

![StarTree Cloud Screen](/images/thirdeye/thirdeye1.png "StarTree Cloud")

**Note:** If you don't see the ThirdEye link active, you may need to contact [StarTree support](support.startree.ai).

Click **ThirdEye**. 

You should see something like this:

![ThirdEye Screen](/images/thirdeye/thirdeye2.png "ThirdEye Start Page")

### 2 - Connect to a dataset

Now that we have access to the ThridEye portal, we'll set up our data for ThirdEye.

Click **Configuration** in the menu.

![ThirdEye Screen](/images/thirdeye/thirdeye3.png "ThirdEye Data Configuration Page")

Select the **Create** button, and then select the **Onboard Dataset** option.

For this challenge, we'll select the existing Apache Pinot source, called **pinot**.

Then, we'll select a dataset available to us. For this challenge, let's select **websiteAnomalies**. 

**Note:** If you're using a shared environment, use one of the websiteAnomalies(x).

![ThirdEye Screen](/images/thirdeye/thirdeye4.png "ThirdEye Data Configuration Page")

Now, select Submit.

That's it! You've configured a datasource for anomaly detection with ThirdEye.

### 3 - Create Alert

Next, we will create an alert. Let's start by selecting **Alert** from the left menu.

![ThirdEye Screen](/images/thirdeye/thirdeye5.png "ThirdEye Alert Configuration Page")

This will take you to a page where you can select one a type of alert to create.

You can choose from the following alert types:

- Basic alert
- Multi-dimensional alert

Dimension exploration gives you the ability to create alerts for every value of a certain dimension or combination of dimensions.

Here's the visual:

![ThirdEye Screen](/images/thirdeye/thirdeye6.png "ThirdEye Alert Configuration Page")

For our porposes, we will choose the Multi-dimensional alert. Next, select the CoHort recommender.

![ThirdEye Screen](/images/thirdeye/thirdeye7.png "ThirdEye Alert Configuration Page")

At this point, you should be able to create an alert using the dataset you onboarded.

Here's what we will be using for each of the values:

1. Dataset: The dataset you onboarded
2. Metric: Let's use click
3. Aggregation function: Let's use COUNT
4. Dimensions: Let's use country, browser and platform
5. Date range: Let's narrow it down to 2021
6. Query filter: Ignore for now
7. Contribution percentage: Let's leave it at 5%.

![ThirdEye Screen](/images/thirdeye/thirdeye8.png "ThirdEye Alert Configuration Page")

Let's select **Generate Dimensions to Monitor** to see what your dimensions look like.

You should see something like this:

![ThirdEye Screen](/images/thirdeye/thirdeye9.png "ThirdEye Alert Configuration Page")

Now, let's select all of the dimensions, and click **Create Multi-dimension** alert.

![ThirdEye Screen](/images/thirdeye/thirdeye10.png "ThirdEye Alert Configuration Page")

You should now be able to select the granularity. The default is Daily, but you can change it. Load the chart to see what the pattern looks like. You can also change the date range to see what shows up.

Choose **SUM** as the Aggregation function, and hourly as the granularity, reload preview, and scroll down to country area.  You'll notice some spikes.

![ThirdEye Screen](/images/thirdeye/thirdeye11.png "ThirdEye Alert Configuration Page")

For our alert, I am going to choose avg daily.
Select Next to move to the algorithm selection.

I am going to select the StarTree-ETS Rule.

![ThirdEye Screen](/images/thirdeye/thirdeye12.png "ThirdEye Alert Configuration Page")

Select the **Next** button, which takes you to the Tune alert page.
Here, you can adjust the sensivity, seasonality, and lookback period. You can load chart to see the alerts that show up based on your tuning.

For our scenario, we will pick high sensitivity & the rest default values.

![ThirdEye Screen](/images/thirdeye/thirdeye13.png "ThirdEye Alert Configuration Page")

Select **Next** to move to the anomaly filter page. Here, you can select the Filters and sensitivity button to adjust your anomaly detection. Examples are adding exception, such as don't monitor on weekends etc.

![ThirdEye Screen](/images/thirdeye/thirdeye14.png "ThirdEye Alert Configuration Page")

For this scenario, I am not going to set up any filter.
Select **Next**, provide a meaningful name, and save.

Voila! You have created your first alert!

### 4 - Examine anomalies

Now that we have created an alert, let's dive into how to look at your anomalies.

From the Alert menu, select the alert you just created.

You should see somthing like this:

![ThirdEye Screen](/images/thirdeye/thirdeye15.png "ThirdEye Examine Anomalies Page")

You can click on the **View Details** link to see the anomalies for a particular set of dimensions:

![ThirdEye Screen](/images/thirdeye/thirdeye16.png "ThirdEye Examine Anomalies Page")

You can click on individual anomalies, or select a section to view it in detail.

Let's click on an anomaly.

![ThirdEye Screen](/images/thirdeye/thirdeye17.png "ThirdEye Examine Anomalies Page")

Select the **Investigate Anomaly** button to do some root cause analysis.

![ThirdEye Screen](/images/thirdeye/thirdeye18.png "ThirdEye Examine Anomalies Page")

Here, you can look at the heatmap, the top contributors, and events. We will talk about events in the next exercise.  

The heatmaps show you what contributing fators were related to the anomaly. Blue indicates higher than normal numbers, red indicates lower than normal numbers, and grey is the baseline.

Top contributors shows you what caused the anomaly.

You also have the option to tag this as "real" or false positive.

From the **Is this an anomaly** drop-down list, choose an option that fits your scenario.

You can save the investigation, revisit later, or share it with someone on your team.

### 5 - Create Events

Now let's create an event.

Navigate to the configuration menu, and select the **Events** tab.

![ThirdEye Screen](/images/thirdeye/thirdeye19.png "ThirdEye Events Page")

Select **Create**, and then **Create Event**.

Enter a name, type (string), and start and end dates.

Optionally, you can add some metadata tags. These can be used for catagorization purposes. Click **Create event** to save.

![ThirdEye Screen](/images/thirdeye/thirdeye20.png "ThirdEye Events Page")

To use a created event, on the Anomalies page, choose the Events tab, and associate the event to the anomaly.

![ThirdEye Screen](/images/thirdeye/thirdeye21.png "ThirdEye Events Page")

### 6 - Create subscription groups

Let's now create subscription groups and associate some alert with them.

From the Configuration menu, select **Subscription Groups**. Select **Create Subscription Group**.

Enter the name and schedule. You can either use cron syntax or use the UI to set up the schedule.

You can also add emails, slack channels or use a webhook to connect to the subscription group.

![ThirdEye Screen](/images/thirdeye/thirdeye22.png "ThirdEye Subscription Groups Page")

Select the **Next** button to set up the alerts you want to be notified on. Click **Save** to save your subscription group.

When you create new alerts, you can use the existing subscription groups to add the alert notification to.

![ThirdEye Screen](/images/thirdeye/thirdeye23.png "ThirdEye Subscription Groups Page")

Voila! You should now recieve alerts when anomalies happen!

### 7 - Tear down

From the Alerts menu, select and delete any alerts you have created.
Fom the Configuration menu, select and delete:

1. Subscription Groups
2. Events
3. Datasets
