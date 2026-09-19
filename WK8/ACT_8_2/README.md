# Online Notification System Using the Factory Method Pattern

## Problem Statement

An organisation needs a Notification System that can send notifications
by Email, SMS, and Push Notification. Each notification type has a
`send()` method.

The task is to use the Factory Method Pattern so the client never
creates `Email()`, `SMS()`, or `Push()` objects directly.

## Requirements

1. `Notification` — abstract product with an abstract `send()` method.
2. `EmailNotification`, `SMSNotification`, `PushNotification` —
   concrete products, each implementing `send()`.
3. `NotificationFactory` — abstract factory with an abstract
   `create_notification()` method.
4. `EmailFactory`, `SMSFactory`, `PushFactory` — concrete factories,
   each returning its own notification type.
5. A client that uses only the factories and `send()`.

## How It Works

- `Notification` is the rule book: every notification must have
  `send()`. It is abstract, so it cannot be created directly.
- `EmailNotification`, `SMSNotification` and `PushNotification` each
  provide their own `send()`.
- `NotificationFactory` is the rule book for factories: every factory
  must have `create_notification()`.
- `EmailFactory`, `SMSFactory` and `PushFactory` each create one
  specific notification. They are the only place the notification
  classes are instantiated.
- The client picks a factory, calls `create_notification()`, then calls
  `send()`. To switch from Email to SMS, only the factory changes. To
  add a new type, add one product class and one factory; existing code
  stays untouched.

## Running the Program

```bash
python main.py
```

### Expected Output

```
Sending EMAIL: Your order has been confirmed.
Sending SMS: Your OTP is 482913.
Sending PUSH notification: You have a new message.

--- Sending the same message through every factory ---
Sending EMAIL: System maintenance tonight at 10 PM.
Sending SMS: System maintenance tonight at 10 PM.
Sending PUSH notification: System maintenance tonight at 10 PM.
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
