import java.io.UnsupportedEncodingException;
import java.util.Scanner;
//javac -encoding utf-8 LuanmaCl.java
public class LuanmaCl {

	public static void main(String[] args) throws UnsupportedEncodingException {
		// TODO Auto-generated method stub
		LuanmaCl U = new LuanmaCl();
		String u = U.getStrUTF8();
		System.out.println(u);
		LuanmaCl G = new LuanmaCl();
		String g = G.getStrGB2312();
		System.out.println(g);
	}
	
	private String getStrUTF8() throws UnsupportedEncodingException {
		System.out.println("utf-8请输入需要转换的字符串：");
		Scanner in = new Scanner(System.in);
		String out = in.nextLine();
		String relout = java.net.URLDecoder.decode(out,"UTF-8");
		return relout;
	}
	
	private String getStrGB2312() throws UnsupportedEncodingException {
		System.out.println("gb2312请输入需要转换的字符串：");
		Scanner in = new Scanner(System.in);
		String out = in.nextLine();
		String relout = java.net.URLDecoder.decode(out,"gb2312");
		return relout;
	}

}
