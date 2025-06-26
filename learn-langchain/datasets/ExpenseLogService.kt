package com.irayspace.fleetmanagement.expenselog

import java.util.concurrent.atomic.AtomicLong
import org.springframework.stereotype.Service

import com.irayspace.fleetmanagement.expenselog.exception.ExpenseLogNotFoundException


@Service
class ExpenseLogService {

    private val db = mutableMapOf<Long, ExpenseLog>()
    private val idGenerator = AtomicLong(0)

    fun getAll(): List<ExpenseLog> = db.values.toList()

    fun getById(id: Long): ExpenseLog = db[id] ?: throw ExpenseLogNotFoundException("Expense Log $id not found")

    fun deleteById(id: Long) {
        getById(id)
        db.remove(id)
    }

    fun create(expenseLog: ExpenseLog): ExpenseLog {
        val id = idGenerator.incrementAndGet()
        val newExpenseLog = expenseLog.copy(id = id)
        db[id] = newExpenseLog
        return newExpenseLog
    }

    fun update(expenseLog: ExpenseLog): ExpenseLog {
        val id = expenseLog.id
        val existing = getById(id)
        val updatedExpenseLog = expenseLog.copy(id = id)
        db[id] = updatedExpenseLog
        return updatedExpenseLog
    }

}