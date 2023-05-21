import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;

public class Huffman {
    private Node root;
    private final String text;
    private Map<Character, Integer> characterfreq;
    private final Map<Character, String> huffmancode;

    public Huffman(String txt) {

        text = txt;
        fillCharFrequenciesMap();
        huffmancode = new HashMap<>();

    }

    public void print() throws FileNotFoundException {
        PrintWriter output_file1=new PrintWriter("C:\\Users\\Youssef Dieaa\\IdeaProjects\\M_huffman\\f.txt");
        output_file1.println("your guide to know the symbol code : "+"\n");
        for (Map.Entry<Character,String> entry : huffmancode.entrySet())
         System.out.println(entry.getKey()+" : " + entry.getValue());
    }

    private void fillCharFrequenciesMap() {
        int counter = 0;
        characterfreq = new HashMap<>();
        for (char chr : text.toCharArray()) {
            Integer intger = characterfreq.get(chr);
            characterfreq.put(chr, intger != null ? intger + 1 : 1);
        }

    }

    public String encode() {
        Queue<Node> queue = new PriorityQueue<>();
        characterfreq.forEach(((character, frequency) -> queue.add(new Leaf(character, frequency))));

        while (queue.size() > 1) {
            queue.add(new Node(queue.poll(), queue.poll()));
        }

        genertaehuffmancode(root = queue.poll(), "");
        return getencodedtxt();
    }

    public String decode(String encodedtxt) {
        StringBuilder sb = new StringBuilder();
        Node current = root;
        for (char chr : encodedtxt.toCharArray()) {
            current = chr == '0' ? current.getleft() : current.getright();
            if (current instanceof Leaf) {
                sb.append(((Leaf) current).getCharcter());
                current = root;
            }

        }

        return sb.toString();
    }

    private void genertaehuffmancode(Node node, String code) {
        if (node instanceof Leaf) {

            huffmancode.put(((Leaf) node).getCharcter(), code);
            return;

        }
        genertaehuffmancode(node.getleft(), code.concat("0"));
        genertaehuffmancode(node.getright(), code.concat("1"));
    }

    private String getencodedtxt() {
        StringBuilder sb = new StringBuilder();
        for (char chr : text.toCharArray()) {
                sb.append(huffmancode.get(chr));

        }
        return sb.toString();
    }
}
