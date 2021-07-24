from time import sleep
from json import dumps
from kafka import KafkaProducer


app = Flask(__name__)

@app.route("/producer")
def kafkaProducer(jsonStr):
    bootstrap_servers = ['0.0.0.0:9092']

    # Define topic name where the message will publish
    topicName = 'First_Topic'

    # Initialize producer variable
    #producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    producer.send(topicName,jsonStr)
    producer.flush()
    producer.close()

#@app.route("/consumer")
#def 

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, host="0.0.0.0",port=8000)



