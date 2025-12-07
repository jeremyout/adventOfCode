/* --- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?

*/


using System.IO;
using System.Runtime.CompilerServices;

string filePath = "../day1input.txt"; 
try
{
    string[] fileContents = File.ReadAllLines(filePath);
    // File.AppendAllText("output.txt",$"Total lines read: {fileContents.Length}\n");

    int totalZeros = 0;
    int dialPosition = 50;

    for (int i = 0; i < fileContents.Length; i++)
    {
        // File.AppendAllText("output.txt",$"\n\n\nProcessing new line, total zeros is {totalZeros}, dial position is {dialPosition}, currently processing {fileContents[i]}\n");

        bool startsWithL = fileContents[i].StartsWith('L');
        bool startsWithR = fileContents[i].StartsWith('R');

        if (!startsWithL && !startsWithR)
        {
            throw new Exception("Line doesn't start with L or R");
        }
        // Check line to make sure it starts with only 1 
        if (!int.TryParse(fileContents[i].Substring(1), out int result))
        {
            throw new Exception($"The substring '{fileContents[i].Substring(1)}' cannot be parsed as an integer.");
        }


        while (result >= 100)
        {
            // File.AppendAllText("output.txt",$"Result is currently {result}, about to decrement 100 and add to totalZeros\n");
            totalZeros++;
            // File.AppendAllText("output.txt",$"Total zeros is {totalZeros} after increment in the while loop\n");
            result -= 100;
        }

        if (result != 0)
        {
            if (startsWithL)
            {
                // File.AppendAllText("output.txt",$"Subtracting {result} from current dial position\n");
                if (dialPosition == 0)
                {
                    // File.AppendAllText("output.txt","Dial position is zero, subtracting without logging zero\n");
                    dialPosition = 100 - result;
                }
                else if (result > dialPosition)
                {
                    // File.AppendAllText("output.txt","Will roll past 0, calculating delta\n");
                    int delta = Math.Abs(dialPosition-result);
                    // File.AppendAllText("output.txt",$"Delta calculated to be {delta}\n");
                    dialPosition = 100 - delta;
                    if (dialPosition != 0)
                    {
                        totalZeros++;
                        // File.AppendAllText("output.txt",$"Subtracted enough to roll past zero, incremented total zeros to {totalZeros}\n");
                    }
                } 
                else
                {
                    dialPosition -= result;
                }
            } 
            else if (startsWithR)
            {
                // File.AppendAllText("output.txt",$"Adding {result} to current dial position\n");
                if (dialPosition + result > 99)
                {
                    // File.AppendAllText("output.txt","Will roll past 99, calculating delta\n");
                    int delta = dialPosition + result  - 100;
                    // File.AppendAllText("output.txt",$"Delta calculated to be {delta}\n");
                    dialPosition = delta;
                    if (dialPosition > 0)
                    {
                        totalZeros++;
                        // File.AppendAllText("output.txt",$"Added enough to roll past 99, incremented total zeros to {totalZeros}\n");
                    }
                }
                else
                {
                    dialPosition += result;
                }
            }

            // File.AppendAllText("output.txt",$"Dial position is now at {dialPosition}\n");

            if (dialPosition == 0)
            {
                totalZeros++;
                // File.AppendAllText("output.txt",$"total zeros incremented to {totalZeros}");
            }
        }
    }
    // File.AppendAllText("output.txt",$"Dial position landed onand passed zero {totalZeros} times\n");
    Console.WriteLine($"Dial position landed on and passed zero {totalZeros} times\n");
}
catch (IOException e)
{
    // File.AppendAllText("output.txt",$"Error reading file: {e.Message}\n");
}