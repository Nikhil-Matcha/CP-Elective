/**
 * This is JUnit that tests the fixMostlyMagicSquare method that is available in FixMostlyMagicSquare class.
 * This contains 1 testcase.
 * 
 * Please don't run this file.
 * You can add your own test cases to this file by just copy and paste the last three 
 * lines of the code (TestCase1).
 * 
 * @author: Siva Sankar
 */

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class TestJUnit {
   @Test
   public void testCase1() {
      assertArrayEquals("1.", new int[][]{{2, 7, 6}, {9, 5, 1}, {4, 3, 8}}, new FixMostlyMagicSquare().fixMostlyMagicSquare(new int[][]{{2, 7, 9}, {9, 5, 1}, {4, 3, 8}}));
      assertArrayEquals("1.", new int[][]{{16, 3, 2, 13}, {5, 10, 11, 8}, {9, 6, 7, 12},{4, 15, 14, 1}}, new FixMostlyMagicSquare().fixMostlyMagicSquare(new int[][]{{16, 3, 2, 13}, {5, 10, 11, 18}, {9, 6, 7, 12},{4, 15, 14, 1}}));
   }
}
