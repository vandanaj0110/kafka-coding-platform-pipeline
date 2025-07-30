# Kafka Coding Platform Pipeline

A real-time data streaming pipeline using Apache Kafka to process submissions, competitions, and solutions from an online coding platform.

## 🎯 Overview

This project implements a producer-consumer pipeline that processes three types of events:
- **Problems**: User submissions to coding problems
- **Competitions**: Contest submissions with time tracking
- **Solutions**: Public solution sharing with upvotes

<img width="846" height="468" alt="image" src="https://github.com/user-attachments/assets/e91853b2-0be7-4655-97e8-cedb8a64a3d5" />

## 🏗️ Architecture

- **1 Producer**: Streams input data to Kafka topics
- **3 Consumers**: Process data for different client requirements
- **3 Topics**: Configurable topic names via command line

## 📊 Client Requirements

### Client 1: Platform Analytics
- Most frequently used programming language
- Most difficult category (lowest pass rate)

### Client 2: Competition Leaderboards
- Points calculation per competition
- User rankings with detailed scoring

### Client 3: Community & ELO Ratings
- Best contributor (highest upvotes)
- User ELO ratings based on performance

## 📤 Output Format

All outputs are JSON formatted with specific schemas for each client's requirements.

## 🔧 Key Features

- **Real-time Processing**: Stream-based data handling
- **Multi-client Support**: Independent consumer processing
- **Flexible Topics**: Configurable Kafka topic names
- **Scoring Systems**: Complex point calculations for competitions and ELO

## ⚡ Requirements

- Apache Kafka
- kafka-python library
- Python 3.x

## 📝 Allowed Modules
- `kafka`
- `sys`
- `json`
- `math`
