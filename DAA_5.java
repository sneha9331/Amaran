import java.util.*;
public class DAA_5{
    static int n;
    static boolean[] cols,leftdiagonal , rightdiagonal;
    static int [] position;
    
    static boolean placeQueen(int row){
        if(row==n)
           return true;
        if(position[row]!=-1)
            return placeQueen(row+1);
        
        for(int j=0;j<n;j++){
            if(cols[j]||rightdiagonal[row+j]||leftdiagonal[row-j+n-1])
                continue;
            cols[j]=true;
            rightdiagonal[row+j]=true;
            leftdiagonal[row-j+n-1]=true;
            position[row]=j;
            
            if(placeQueen(row+1))
                return true;
            
            cols[j]=false;
            rightdiagonal[row+j]=false;
            leftdiagonal[row-j+n-1]=false;
            position[row]=-1;    
            
       }
       return false;
    }
    static char [][] nQueenWithFirstPlace(int size,int firstrow,int firstcol){
        n=size;
        cols= new boolean[n];
        leftdiagonal = new boolean[2*n];
        rightdiagonal = new boolean[2*n];
        position = new int[n];
        Arrays.fill(position,-1);
        
        position[firstrow]=firstcol;
        cols[firstcol]=true;
        rightdiagonal[firstrow+firstcol]=true;
        leftdiagonal[firstrow-firstcol+n-1]=true;
        
        if(!placeQueen(0))
            return null;
        
        char [][] board =new char[n][n];
        for(int i=0;i<n;i++)
            Arrays.fill(board[i],'.');
            
        for(int i = 0 ;i<n ; i++)
            board[i] [position[i]]='Q';
        return board;
    }
    static void printBoard(char[][]board){
        if(board==null){
            System.out.print("No solution exist");
            return;
        }
        for(int i=0 ;i<board.length;i++){
            for(int j=0;j<board[i].length;j++){
                System.out.print(board[i][j]+"");
            }
            System.out.println();
        }
    }
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the board size:");
        int n = sc.nextInt();
        
        System.out.print("Enter the place of Queen(row" + n +"):");
        int firstrow = sc.nextInt()-1;
        
        System.out.print("Enter the place of Queen(col" + n +"):");
        int firstcol = sc.nextInt()-1;
        
        char [][] board = nQueenWithFirstPlace(n,firstrow,firstcol);
        System.out.println("final N-Queen Matrix:");
        printBoard(board);
        sc.close();
        
    }
    
}