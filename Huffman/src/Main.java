import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {

    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String encoded = null;
        String decoded = null;
        Huffman d = new Huffman("ww");
        Path fileName = Path.of(
                "C:\\Users\\Youssef Dieaa\\IdeaProjects\\Huffman\\ok.txt");
        try {
            System.out.println("plz enter the line you want to encode it");
            String inputt;
            inputt = reader.readLine();
            Files.writeString(fileName, inputt);
            FileReader readerr = new FileReader("C:\\Users\\Youssef Dieaa\\IdeaProjects\\Huffman\\ok.txt");
            BufferedReader bufferedReader = new BufferedReader(readerr);
            String l;
            PrintWriter output_file = new PrintWriter("C:\\Users\\Youssef Dieaa\\IdeaProjects\\Huffman\\ok1.txt");
            while ((l = bufferedReader.readLine()) != null) {
                Huffman m = new Huffman(l);
                encoded = m.encode();
                decoded = m.decode(encoded);
                m.print();
            }
            readerr.close();

            output_file.println("your encoded code is : " + encoded);
            output_file.println("\n");
            output_file.println("your decoded code is : " + decoded);

            output_file.close();

        } catch (IOException e) {
            e.printStackTrace();

        }
    }
}
