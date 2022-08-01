import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Arrays;

public class Point{
    long x;
    long y;
    
    public Point(long x, long y){
        this.x = x;
        this.y = y;
    }
    
    
    public String toString(){
        return Long.toString(x) + "," + Long.toString(y);
    }
}

class Solution {
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        HashSet<String> hash = new HashSet<>();
        
        for(int i = 0; i < line.length - 1; ++i){
            long a = line[i][0];
            long b = line[i][1];
            long e = line[i][2];
            for(int j = 1; j < line.length; ++j){
                long c = line[j][0];
                long d = line[j][1];
                long f = line[j][2];
                if(a*d-b*c == 0) continue;
                long xMother = (b*f-e*d);
                long xSon = (a*d-b*c);
                if(xMother % xSon != 0) continue;
                long yMother = (e*c-a*f);
                long ySon = (a*d-b*c);
                if(yMother % ySon != 0) continue;
                long x = xMother/xSon;
                long y = yMother/ySon;
                points.add(new Point(x,y));
                Point p = new Point(x,y);
                hash.add(p.toString());
                
            }
        }
        long xMax = points.get(0).x;
        long xMin = points.get(0).x;
        long yMax = points.get(0).y;
        long yMin = points.get(0).y;
      
        
        for(int i = 0; i < points.size();++i){
            
            Point p = points.get(i);
           
            xMax = Math.max(xMax, p.x);
            yMax = Math.max(yMax, p.y);
            xMin = Math.min(xMin, p.x);
            yMin = Math.min(yMin, p.y);
           
        }
        long width = xMax - xMin + 1;
        long height = yMax - yMin + 1;
        String[][] answer = new String[(int)height][(int)width];
      
        String[] result = new String[(int)height];
        
        for(Long i = xMin; i <= xMax; ++i){
            for(Long j = yMax; j >= yMin; --j){
                if(hash.contains(Long.toString(i)+","+Long.toString(j)))
                    answer[(int)(yMax-j)][(int)(i-xMin)] = "*";
                else
                    answer[(int)(yMax-j)][(int)(i-xMin)] = ".";
            }
        }
        int i = 0;
        for(String[] an : answer){
            String arrString = String.join("",an);
            result[i++] = arrString;
        }
            
        return result;
    }
}public class 교점에별만들기 {
    
}
