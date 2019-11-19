/* Run these commands to use the given code

# Compile the java program
javac -cp "/usr/local/kafka/libs/*" *.java

# Run the java program and send message to kafka normaly
java -cp "/usr/local/kafka/libs/*":. SampleProducer normal

# Run the java program and send message to kafka synchronously
java -cp "/usr/local/kafka/libs/*":. SampleProducer sync

# Run the java program and send message to kafka asynchronously
java -cp "/usr/local/kafka/libs/*":. SampleProducer async

*/


import java.util.*;
import java.util.Scanner; 
import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.clients.producer.ProducerConfig;


class SampleProducer {

    private static class DemoProducerCallBack implements Callback{
        @Override
        public void onCompletion(RecordMetadata recordMetadata, Exception e){
            if (e != null) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String[] args){

        String sendType = args[0]; 

        Properties kafkaProps = new Properties();
        kafkaProps.put("bootstrap.servers", "localhost:9092");
    
        // Serializer for message key       
        kafkaProps.put(
            "key.serializer",
            "org.apache.kafka.common.serialization.StringSerializer");
        
        // Serializer for message value
        kafkaProps.put(
            "value.serializer",
            "org.apache.kafka.common.serialization.StringSerializer");

        //Set the number of retries - retries
        kafkaProps.put(ProducerConfig.RETRIES_CONFIG, 3);

        //Request timeout - request.timeout.ms
        kafkaProps.put(ProducerConfig.REQUEST_TIMEOUT_MS_CONFIG, 15_000);

        //Only retry after one second.
        kafkaProps.put(ProducerConfig.RETRY_BACKOFF_MS_CONFIG, 1_000);

        KafkaProducer producer = new KafkaProducer<String, String>(kafkaProps); 

        DemoProducerCallBack producerCallback = new DemoProducerCallBack();

        ProducerRecord<String, String> record =
            new ProducerRecord<>(
                "test",
                "new_key_testing1",
                "value_hello");

        try {
            if (sendType.equals("sync")){
                System.out.println("Sending message synchronously.");
                producer.send(record).get();
                System.out.println("Message sent synchronously.");
            }
            else if (sendType.equals("async")){
                System.out.println("Sending message asynchronously.");
                producer.send(record, producerCallback);
                System.out.println("Message sent asynchronously.");
            }
            else if (sendType.equals("normal")) {
                System.out.println("Sending message normally.");
                producer.send(record);
                System.out.println("Message sent normally.");
            }
            else {
                System.out.println("Invalid sendType provided. Sending message normally.");
                producer.send(record);
                System.out.println("Message sent normally.");
            }
            
            producer.close();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    };

};