package com.example.myfirstapp

import android.annotation.SuppressLint
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import android.widget.Toast.LENGTH_LONG
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {
    var successCombinations : Array<Int> = arrayOf(0,0,0,0,0,0,0,0)
    var gameCount : Array<Int> = arrayOf(0,0)
    lateinit var cells : Array<View>
    var Turn : Boolean = true
    var GameEnded : Boolean = false

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var cellsInit : Array<View> = arrayOf(
            findViewById(R.id.button1),
            findViewById(R.id.button2),
            findViewById(R.id.button3),
            findViewById(R.id.button4),
            findViewById(R.id.button5),
            findViewById(R.id.button6),
            findViewById(R.id.button7),
            findViewById(R.id.button8),
            findViewById(R.id.button9)
        )

        cells = cellsInit
    }//----------------------------------------init-shit----------------------------------------------<


    fun refreshCombinationValues(){
        successCombinations[0] = getSide(cells[0]) + getSide(cells[1]) + getSide(cells[2])
        successCombinations[1] = getSide(cells[3]) + getSide(cells[4]) + getSide(cells[5])  //horizontal
        successCombinations[2] = getSide(cells[6]) + getSide(cells[7]) + getSide(cells[8])

        successCombinations[3] = getSide(cells[0]) + getSide(cells[3]) + getSide(cells[6])
        successCombinations[4] = getSide(cells[1]) + getSide(cells[4]) + getSide(cells[7])  //vertical
        successCombinations[5] = getSide(cells[2]) + getSide(cells[5]) + getSide(cells[8])

        successCombinations[6] = getSide(cells[0]) + getSide(cells[4]) + getSide(cells[8])  //diagonal
        successCombinations[7] = getSide(cells[2]) + getSide(cells[4]) + getSide(cells[6])
    }
    fun getSide(view: View): Int{
        return when ((view as? Button)?.text)
        {
            "X" -> 1
            "O" -> -1
            else -> {0}
        }
    }

    fun cellPress(view: View){
        if (GameEnded)
            return
        if ((view as? Button)?.text == "")
        {
            (view as? Button)?.text = if(Turn){ "X" } else{ "O" }
            Turn = !Turn
        }

        refreshCombinationValues()
        checkGame()
    }

    fun checkGame(){
        val cellsDataArr = Array(cells.size) { i -> (cells[i] as? Button)?.text.toString() }

        if (3 in successCombinations)
        {
            endGame(successCombinations.indexOf(3), "X")
        }
        else if(-3 in successCombinations)
        {
            endGame(successCombinations.indexOf(-3), "O")
        }
        else if("" !in cellsDataArr)
        {
            endGame(404, "-")
        }
    }

    fun endGame(index: Int, winner: String){
        lateinit var text : String

        when (winner)
        {
            "X" -> { text = "X wins!"; gameCount[0] += 1 }
            "O" -> { text = "O wins!"; gameCount[1] += 1 }
            "-" -> { text = "Draw!" }
        }
        for (i in cells)
        {
            if ((i as? Button)?.text == "")
                (i as? Button)?.text = "-"
        }

        GameEnded = true
        val butToast = Toast.makeText(applicationContext, text, LENGTH_LONG)
        butToast.show()
        countText.text = "X: ${gameCount[0]}  |  O: ${gameCount[1]}"
        searchAndLight(index)   // <-- optional
    }

    fun searchAndLight(index: Int){
        when (index)
        {
            0 -> {setButtonsColor(arrayOf(cells[0], cells[1], cells[2]))}
            1 -> {setButtonsColor(arrayOf(cells[3], cells[4], cells[5]))}
            2 -> {setButtonsColor(arrayOf(cells[6], cells[7], cells[8]))}

            3 -> {setButtonsColor(arrayOf(cells[0], cells[3], cells[6]))}
            4 -> {setButtonsColor(arrayOf(cells[1], cells[4], cells[7]))}
            5 -> {setButtonsColor(arrayOf(cells[2], cells[5], cells[8]))}

            6 -> {setButtonsColor(arrayOf(cells[0], cells[4], cells[8]))}
            7 -> {setButtonsColor(arrayOf(cells[2], cells[4], cells[6]))}

            else -> return
        }
    }
    fun setButtonsColor(Arr : Array<View>) {
        for (i in Arr)
            (i as? Button)?.setTextColor(Color.parseColor("#B8E36F"))
    }

    fun restart(view: View)
    {
        for (i in cells){
            (i as? Button)?.setTextColor(Color.parseColor("#FFFFFFFF"))
            (i as? Button)?.text = ""
        }
        GameEnded = false
        Turn = true
    }
}